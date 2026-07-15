import hashlib
import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from scripts.prepare_corpus import (
    CorpusError,
    fetch_restricted_sources,
    prepare_full_source_corpus,
    prepare_summary_corpus,
    validate_source_hygiene,
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class PrepareCorpusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "repo"
        for directory in (
            "source_documents/00_meta",
            "source_documents/public_references",
            "source_documents/synthetic_internal",
            "original_public_sources",
        ):
            (self.root / directory).mkdir(parents=True, exist_ok=True)

        (self.root / "source_documents/00_meta/engagement.md").write_text("# Engagement\n")
        (self.root / "source_documents/00_meta/source.md").write_text("# Source statement\n")
        (self.root / "source_documents/public_references/ref_a.md").write_text("# Reference A\n")
        (self.root / "source_documents/public_references/ref_b.md").write_text("# Reference B\n")
        (self.root / "source_documents/synthetic_internal/doc_a.md").write_text("# Internal A\n")
        (self.root / "source_documents/synthetic_internal/doc_b.md").write_text("# Internal B\n")

        allowed = self.root / "original_public_sources/allowed.pdf"
        allowed.write_bytes(b"allowed-original")
        (self.root / "original_public_sources/manifest.json").write_text(
            json.dumps(
                {
                    "schema_version": "test",
                    "files": [
                        {
                            "filename": allowed.name,
                            "sha256": sha256(allowed),
                            "official_url": "https://example.test/allowed.pdf",
                        }
                    ],
                }
            )
        )

        self.remote = Path(self.temp.name) / "restricted.pdf"
        self.remote.write_bytes(b"restricted-original")
        (self.root / "restricted_public_sources.json").write_text(
            json.dumps(
                {
                    "schema_version": "test",
                    "files": [
                        {
                            "filename": self.remote.name,
                            "sha256": sha256(self.remote),
                            "official_url": self.remote.as_uri(),
                        }
                    ],
                }
            )
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_summary_mode_copies_only_canonical_source_documents(self):
        target = Path(self.temp.name) / "summary"
        manifest_path = prepare_summary_corpus(self.root, target)

        copied = sorted(str(path.relative_to(target)) for path in target.rglob("*") if path.is_file())
        self.assertEqual(
            copied,
            [
                "00_meta/engagement.md",
                "00_meta/source.md",
                "public_references/ref_a.md",
                "public_references/ref_b.md",
                "synthetic_internal/doc_a.md",
                "synthetic_internal/doc_b.md",
            ],
        )
        self.assertFalse((target / "manifest.json").exists())
        manifest = json.loads(manifest_path.read_text())
        self.assertEqual(manifest["mode"], "summary")
        self.assertEqual(manifest["file_count"], 6)
        self.assertNotIn("source_root", manifest)
        self.assertEqual(manifest["corpus_directory"], target.name)
        self.assertNotIn(str(self.root), json.dumps(manifest))

    def test_full_source_mode_replaces_reference_records_with_originals(self):
        cache = Path(self.temp.name) / "cache"
        fetch_restricted_sources(self.root, cache)
        target = Path(self.temp.name) / "full"
        manifest_path = prepare_full_source_corpus(self.root, target, cache)

        copied = sorted(str(path.relative_to(target)) for path in target.rglob("*") if path.is_file())
        self.assertEqual(
            copied,
            [
                "00_meta/engagement.md",
                "00_meta/source.md",
                "external_originals/allowed.pdf",
                "external_originals/restricted.pdf",
                "synthetic_internal/doc_a.md",
                "synthetic_internal/doc_b.md",
            ],
        )
        self.assertFalse((target / "public_references").exists())
        manifest = json.loads(manifest_path.read_text())
        self.assertEqual(manifest["mode"], "full-source")
        self.assertEqual(manifest["external_original_count"], 2)

    def test_full_source_mode_rejects_receipt_from_changed_manifest(self):
        cache = Path(self.temp.name) / "cache"
        fetch_restricted_sources(self.root, cache)
        manifest_path = self.root / "restricted_public_sources.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["files"][0]["sha256"] = "0" * 64
        manifest_path.write_text(json.dumps(manifest))
        target = Path(self.temp.name) / "full"

        with self.assertRaisesRegex(CorpusError, "receipt baseline mismatch"):
            prepare_full_source_corpus(self.root, target, cache)

    def test_hygiene_rejects_yaml_in_canonical_evidence_directories(self):
        bad = self.root / "source_documents/synthetic_internal/doc_a.md"
        bad.write_text("---\ntitle: derived metadata\n---\n# Internal A\n")

        with self.assertRaisesRegex(CorpusError, "YAML frontmatter"):
            validate_source_hygiene(self.root / "source_documents")

    def test_full_source_mode_rejects_hash_mismatch(self):
        cache = Path(self.temp.name) / "cache"
        fetch_restricted_sources(self.root, cache)
        (cache / "restricted.pdf").write_bytes(b"tampered")

        with self.assertRaisesRegex(CorpusError, "SHA-256 mismatch"):
            prepare_full_source_corpus(self.root, Path(self.temp.name) / "full", cache)

    def test_fetch_restricted_sources_verifies_downloaded_hash(self):
        cache = Path(self.temp.name) / "cache"
        fetched = fetch_restricted_sources(self.root, cache)

        self.assertEqual(fetched, [cache / "restricted.pdf"])
        self.assertEqual((cache / "restricted.pdf").read_bytes(), self.remote.read_bytes())
        receipt = json.loads((cache / "download_receipt.json").read_text())
        self.assertEqual(receipt["files"][0]["status"], "unchanged")
        self.assertEqual(receipt["files"][0]["actual_sha256"], sha256(self.remote))

    def test_fetch_keeps_changed_official_source_and_records_hash_drift(self):
        manifest_path = self.root / "restricted_public_sources.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["files"][0]["sha256"] = "0" * 64
        manifest_path.write_text(json.dumps(manifest))
        cache = Path(self.temp.name) / "cache"

        fetched = fetch_restricted_sources(self.root, cache)

        self.assertEqual(fetched, [cache / "restricted.pdf"])
        self.assertEqual((cache / "restricted.pdf").read_bytes(), self.remote.read_bytes())
        receipt = json.loads((cache / "download_receipt.json").read_text())
        record = receipt["files"][0]
        self.assertEqual(record["status"], "changed")
        self.assertEqual(record["reviewed_sha256"], "0" * 64)
        self.assertEqual(record["actual_sha256"], sha256(self.remote))

    def test_fetch_does_not_compare_living_html_hash(self):
        remote_html = Path(self.temp.name) / "living.html"
        remote_html.write_text("<html>current rendering</html>")
        manifest_path = self.root / "restricted_public_sources.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["files"][0].update(
            {
                "filename": "living.html",
                "sha256": "0" * 64,
                "official_url": remote_html.as_uri(),
            }
        )
        manifest_path.write_text(json.dumps(manifest))
        cache = Path(self.temp.name) / "cache"

        fetched = fetch_restricted_sources(self.root, cache)

        self.assertEqual(fetched, [cache / "living.html"])
        receipt = json.loads((cache / "download_receipt.json").read_text())
        record = receipt["files"][0]
        self.assertEqual(record["status"], "not_compared")
        self.assertEqual(record["reviewed_sha256"], "0" * 64)
        self.assertEqual(record["actual_sha256"], sha256(remote_html))

    def test_fetch_sends_an_explicit_user_agent(self):
        payload = b"publisher-file"

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.headers.get("User-Agent") != (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
                ):
                    self.send_response(403)
                    self.end_headers()
                    return
                self.send_response(200)
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, format, *args):
                return

        server = HTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            manifest_path = self.root / "restricted_public_sources.json"
            manifest = json.loads(manifest_path.read_text())
            manifest["files"][0].update(
                {
                    "filename": "publisher.pdf",
                    "sha256": hashlib.sha256(payload).hexdigest(),
                    "official_url": f"http://127.0.0.1:{server.server_port}/publisher.pdf",
                }
            )
            manifest_path.write_text(json.dumps(manifest))
            cache = Path(self.temp.name) / "cache"

            fetched = fetch_restricted_sources(self.root, cache)

            self.assertEqual(fetched, [cache / "publisher.pdf"])
            self.assertEqual((cache / "publisher.pdf").read_bytes(), payload)
        finally:
            server.shutdown()
            thread.join()
            server.server_close()

    def test_fetch_rejects_unsafe_manifest_filenames(self):
        manifest_path = self.root / "restricted_public_sources.json"
        original = json.loads(manifest_path.read_text())
        unsafe_names = [
            "../escape.pdf",
            "/tmp/escape.pdf",
            "nested/file.pdf",
            "nested\\file.pdf",
            "",
        ]
        for index, unsafe in enumerate(unsafe_names):
            with self.subTest(filename=unsafe):
                manifest = json.loads(json.dumps(original))
                manifest["files"][0]["filename"] = unsafe
                manifest_path.write_text(json.dumps(manifest))
                cache = Path(self.temp.name) / f"unsafe-cache-{index}"
                with self.assertRaisesRegex(CorpusError, "unsafe filename"):
                    fetch_restricted_sources(self.root, cache)

    def test_fetch_rejects_symlink_destination(self):
        cache = Path(self.temp.name) / "cache"
        cache.mkdir()
        outside = Path(self.temp.name) / "outside.pdf"
        outside.write_bytes(b"do-not-touch")
        (cache / "restricted.pdf").symlink_to(outside)

        with self.assertRaisesRegex(CorpusError, "symlink"):
            fetch_restricted_sources(self.root, cache)

        self.assertEqual(outside.read_bytes(), b"do-not-touch")

    def test_existing_nonempty_target_is_refused(self):
        target = Path(self.temp.name) / "summary"
        target.mkdir()
        (target / "keep.txt").write_text("do not overwrite")

        with self.assertRaisesRegex(CorpusError, "target directory is not empty"):
            prepare_summary_corpus(self.root, target)


if __name__ == "__main__":
    unittest.main()
