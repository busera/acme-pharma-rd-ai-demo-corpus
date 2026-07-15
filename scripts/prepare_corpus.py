#!/usr/bin/env python3
"""Prepare deterministic ACME Pharma R&D AI corpora for APM/AWP runs."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


class CorpusError(RuntimeError):
    """Raised when corpus preparation would be unsafe or non-reproducible."""


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_manifest(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CorpusError(f"cannot read manifest {path}: {exc}") from exc
    if not isinstance(data.get("files"), list):
        raise CorpusError(f"manifest has no files array: {path}")
    return data


def _ensure_empty_target(target: Path) -> None:
    if target.exists() and any(target.iterdir()):
        raise CorpusError(f"target directory is not empty: {target}")
    target.mkdir(parents=True, exist_ok=True)


def _verify_file(path: Path, expected: str) -> None:
    if not path.is_file():
        raise CorpusError(f"required source is missing: {path}")
    actual = _sha256(path)
    if actual != expected:
        raise CorpusError(
            f"SHA-256 mismatch for {path}: expected {expected}, got {actual}"
        )


def validate_source_hygiene(source_root: Path) -> None:
    """Reject pipeline-derived YAML in canonical evidence directories."""
    for directory in ("public_references", "synthetic_internal"):
        path = source_root / directory
        if not path.is_dir():
            raise CorpusError(f"missing canonical source directory: {path}")
        for document in sorted(path.glob("*.md")):
            if document.read_text(encoding="utf-8").startswith("---\n"):
                raise CorpusError(f"YAML frontmatter is not allowed: {document}")


def _copy_files(source: Path, target: Path) -> None:
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(source)
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)


def _safe_manifest_filename(value: object) -> str:
    if not isinstance(value, str) or not value or value in {".", ".."}:
        raise CorpusError(f"unsafe filename in source manifest: {value!r}")
    candidate = Path(value)
    if candidate.is_absolute() or candidate.name != value or "/" in value or "\\" in value:
        raise CorpusError(f"unsafe filename in source manifest: {value!r}")
    return value


def _safe_child(directory: Path, filename: object) -> Path:
    name = _safe_manifest_filename(filename)
    if directory.is_symlink():
        raise CorpusError(f"symlink cache/source directory is not allowed: {directory}")
    path = directory / name
    if path.is_symlink():
        raise CorpusError(f"symlink destination/source is not allowed: {path}")
    if path.parent.resolve() != directory.resolve():
        raise CorpusError(f"unsafe filename escapes source directory: {name!r}")
    return path


def _target_manifest(target: Path, mode: str, **extra: object) -> Path:
    files = []
    for path in sorted(target.rglob("*")):
        if path.is_file():
            files.append(
                {
                    "path": str(path.relative_to(target)),
                    "bytes": path.stat().st_size,
                    "sha256": _sha256(path),
                }
            )
    payload = {
        "schema_version": "acme-apm-corpus.v1",
        "mode": mode,
        "corpus_directory": target.name,
        "file_count": len(files),
        "files": files,
        **extra,
    }
    manifest_path = target.parent / f"{target.name}.manifest.json"
    manifest_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return manifest_path


def prepare_summary_corpus(repo_root: Path, target: Path) -> Path:
    source_root = repo_root / "source_documents"
    validate_source_hygiene(source_root)
    _ensure_empty_target(target)
    _copy_files(source_root, target)
    return _target_manifest(target, "summary")


def fetch_restricted_sources(repo_root: Path, cache: Path) -> list[Path]:
    manifest = _load_manifest(repo_root / "restricted_public_sources.json")
    cache.mkdir(parents=True, exist_ok=True)
    if cache.is_symlink():
        raise CorpusError(f"symlink cache directory is not allowed: {cache}")
    fetched: list[Path] = []
    receipt_files: list[dict] = []
    for entry in manifest["files"]:
        destination = _safe_child(cache, entry["filename"])
        expected = entry["sha256"]
        temporary = destination.with_suffix(destination.suffix + ".part")
        if temporary.is_symlink():
            raise CorpusError(f"symlink temporary destination is not allowed: {temporary}")
        temporary.unlink(missing_ok=True)
        try:
            user_agent = (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
            )
            request = urllib.request.Request(
                entry["official_url"], headers={"User-Agent": user_agent}
            )
            try:
                with urllib.request.urlopen(request, timeout=120) as response:
                    with temporary.open("wb") as handle:
                        shutil.copyfileobj(response, handle)
            except urllib.error.HTTPError as http_error:
                if http_error.code != 403:
                    raise
                subprocess.run(
                    [
                        "curl",
                        "--location",
                        "--fail",
                        "--silent",
                        "--show-error",
                        "--max-time",
                        "180",
                        "--user-agent",
                        user_agent,
                        "--output",
                        str(temporary),
                        entry["official_url"],
                    ],
                    check=True,
                    timeout=200,
                )
            actual = _sha256(temporary)
            temporary.replace(destination)
        except Exception as exc:
            temporary.unlink(missing_ok=True)
            raise CorpusError(
                f"failed to fetch {entry['filename']} from {entry['official_url']}: {exc}"
            ) from exc
        if destination.suffix.lower() in {".html", ".htm"}:
            status = "not_compared"
        else:
            status = "unchanged" if actual == expected else "changed"
        fetched.append(destination)
        receipt_files.append(
            {
                "filename": destination.name,
                "official_url": entry["official_url"],
                "reviewed_url": entry["official_url"],
                "reviewed_sha256": expected,
                "actual_sha256": actual,
                "bytes": destination.stat().st_size,
                "status": status,
            }
        )
    receipt = {
        "schema_version": "acme-external-download-receipt.v1",
        "downloaded_at": datetime.now(timezone.utc).isoformat(),
        "files": receipt_files,
    }
    (cache / "download_receipt.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    return fetched


def _iter_verified_originals(directory: Path, manifest_path: Path) -> Iterable[Path]:
    manifest = _load_manifest(manifest_path)
    for entry in manifest["files"]:
        path = _safe_child(directory, entry["filename"])
        _verify_file(path, entry["sha256"])
        yield path


def _iter_verified_downloads(directory: Path, manifest_path: Path) -> Iterable[Path]:
    expected_manifest = _load_manifest(manifest_path)
    receipt_path = directory / "download_receipt.json"
    receipt = _load_manifest(receipt_path)
    expected_by_name = {
        _safe_manifest_filename(entry["filename"]): entry
        for entry in expected_manifest["files"]
    }
    receipt_by_name = {
        _safe_manifest_filename(entry["filename"]): entry for entry in receipt["files"]
    }
    if set(receipt_by_name) != set(expected_by_name):
        raise CorpusError(
            f"download receipt does not match restricted source inventory: {receipt_path}"
        )
    for name in sorted(expected_by_name):
        expected_entry = expected_by_name[name]
        receipt_entry = receipt_by_name[name]
        if receipt_entry.get("reviewed_sha256") != expected_entry["sha256"]:
            raise CorpusError(f"receipt baseline mismatch for {name}")
        if receipt_entry.get("official_url") != expected_entry["official_url"]:
            raise CorpusError(f"receipt URL mismatch for {name}")
        path = _safe_child(directory, name)
        _verify_file(path, receipt_entry["actual_sha256"])
        yield path


def prepare_full_source_corpus(
    repo_root: Path, target: Path, restricted_cache: Path
) -> Path:
    source_root = repo_root / "source_documents"
    validate_source_hygiene(source_root)
    _ensure_empty_target(target)

    _copy_files(source_root / "00_meta", target / "00_meta")
    _copy_files(source_root / "synthetic_internal", target / "synthetic_internal")

    external_target = target / "external_originals"
    external_target.mkdir(parents=True, exist_ok=True)
    allowed = list(
        _iter_verified_originals(
            repo_root / "original_public_sources",
            repo_root / "original_public_sources/manifest.json",
        )
    )
    restricted = list(
        _iter_verified_downloads(
            restricted_cache, repo_root / "restricted_public_sources.json"
        )
    )
    for path in [*allowed, *restricted]:
        shutil.copy2(path, external_target / path.name)

    return _target_manifest(
        target,
        "full-source",
        external_original_count=len(allowed) + len(restricted),
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    verify = subparsers.add_parser("verify", help="validate canonical source hygiene")
    verify.set_defaults(action="verify")

    fetch = subparsers.add_parser(
        "fetch-restricted", help="download current restricted originals and write a drift receipt"
    )
    fetch.add_argument("--cache", type=Path, required=True)
    fetch.set_defaults(action="fetch")

    summary = subparsers.add_parser(
        "prepare-summary", help="copy the canonical Markdown corpus"
    )
    summary.add_argument("--target", type=Path, required=True)
    summary.set_defaults(action="summary")

    full = subparsers.add_parser(
        "prepare-full", help="replace summaries with 20 hash-pinned originals"
    )
    full.add_argument("--target", type=Path, required=True)
    full.add_argument("--restricted-cache", type=Path, required=True)
    full.set_defaults(action="full")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    repo_root = args.repo_root.resolve()
    try:
        if args.action == "verify":
            validate_source_hygiene(repo_root / "source_documents")
            print("source hygiene: PASS")
        elif args.action == "fetch":
            files = fetch_restricted_sources(repo_root, args.cache.resolve())
            print(
                f"fetched {len(files)} restricted originals; "
                f"receipt: {args.cache.resolve() / 'download_receipt.json'}"
            )
        elif args.action == "summary":
            manifest = prepare_summary_corpus(repo_root, args.target.resolve())
            print(manifest)
        else:
            manifest = prepare_full_source_corpus(
                repo_root, args.target.resolve(), args.restricted_cache.resolve()
            )
            print(manifest)
    except CorpusError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
