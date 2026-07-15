# AGENTS.md

## Purpose

This repository is a public synthetic evidence pack for preparing ACME Pharma R&D AI audit-planning inputs. ACME Pharma and every internal record, person, supplier, system, use case, and project are fictional.

This repository prepares evidence. It does not contain or run an APM/AWP implementation.

## Non-negotiable source boundaries

- Treat files in `source_documents/synthetic_internal/` as records created by the unit under review.
- Do not add auditor commentary, findings, issue annotations, walkthrough questions, PBC requests, AWP language, generated ratings, or prior-run conclusions to source evidence.
- `source_documents/public_references/` and `source_documents/synthetic_internal/` must not contain pipeline-generated YAML frontmatter.
- Do not silently correct or remove realistic business-owned pending actions, draft states, exceptions, or unresolved decisions.
- Do not invent missing approvals, dates, owners, control operation, or regulatory applicability.
- Do not mix public-reference summaries and their full originals in one run. That duplicates and overweights the same authorities.
- Do not put download receipts, prepared-corpus manifests, logs, configs, or generated outputs inside the evidence directory supplied to a scanner.
- Do not commit publisher-restricted originals from the local download cache.
- The draft PBC request was deliberately removed. Do not recreate it as auditee evidence.

## Organizational baseline

Keep these facts aligned if the synthetic records are changed:

- ACME Pharma: about 50,000 employees globally; R&D: about 9,000.
- Forums and functions: R&D Digital Office, Enterprise AI Governance Office, R&D AI Steering Committee, R&D Data Council, GxP Boundary Review, Supplier Co-Development Review, Research Integrity Committee, Quality and Regulatory Science, Legal/IP, Privacy, Security, Third Party Risk Management, and Procurement.
- Use cases: `UC-RD-001` through `UC-RD-010`.
- Systems: `SYS-AI-001` through `SYS-AI-009`; `UC-RD-008` has no assigned system.
- Project NEURALIS: `UC-RD-003` / `SYS-AI-003`; Translational Medicine business owner; R&D Digital Office product owner; HelixBridge Analytics co-development supplier; controlled development; public literature plus selected restricted internal summaries; GxP boundary pending; no production, regulatory, or submission use.
- Data classes: Public scientific information; Internal research information; Restricted research information; GxP or submission-support information; Personal or sensitive data.
- Derived artifacts inherit the highest source classification until an approved downgrade.
- Lifecycle: intake; classification; design; build/configure; evaluate; release; monitor/change; retire.
- Regulatory drafting remains proposed only; lab-note synthesis remains on hold; candidate ranking remains advisory in a controlled pilot; shadow use remains unofficial.

## Choose one preparation mode

### Mode A: summary corpus

Use for the stable public demonstration set. It contains 2 meta records, 21 attributed public-reference records, and 32 synthetic internal records.

```bash
python3 scripts/prepare_corpus.py verify
python3 scripts/prepare_corpus.py prepare-summary \
  --target ../acme-apm-summary-input
```

The tool writes the evidence directory and an adjacent `acme-apm-summary-input.manifest.json`. Supply only the evidence directory to the APM/AWP scanner.

### Mode B: expanded-source corpus

Use when the run should inspect current official source files instead of the 21 public-reference records.

```bash
python3 scripts/prepare_corpus.py fetch-restricted \
  --cache ../acme-external-source-cache

python3 scripts/prepare_corpus.py prepare-full \
  --restricted-cache ../acme-external-source-cache \
  --target ../acme-apm-full-source-input
```

This mode copies 2 meta records, 32 synthetic internal records, and 20 external originals. It excludes all public-reference summaries to prevent duplicate weighting.

The fetch step:

- downloads current official versions of seven originals that are not redistributed in this repository;
- uses current official URLs from `restricted_public_sources.json`;
- records prior URLs where an official publisher moved an asset;
- records `unchanged` or `changed` for fixed files;
- records `not_compared` for living HTML pages;
- writes actual SHA-256 and byte count to `download_receipt.json`;
- accepts publisher updates but does not accept modification after receipt creation.

The committed 13 redistributable originals and their hashes are under `original_public_sources/`.

## Run handoff

This repository does not prescribe an APM/AWP command. After preparation:

1. Verify the adjacent corpus manifest exists.
2. Record the preparation mode and manifest SHA-256 in the run notes.
3. Point the installed APM/AWP workflow at the prepared evidence directory only.
4. Keep output, logs, state, and caches outside this repository and outside the evidence directory.
5. Treat draft, advisory, vendor, and framework material according to its stated status.
6. Do not treat external criteria as proof that an ACME event occurred or that a control exists or operates effectively.
7. Do not represent `example_outputs/` as output from the current corpus; it is a historical reduced example from the earlier 50-file pack.

## Validation

Run before committing or using the corpus:

```bash
python3 -m unittest discover -s tests -p 'test_prepare_corpus.py' -v
python3 scripts/prepare_corpus.py verify
git diff --check
```

Also verify:

- no YAML frontmatter in public-reference or synthetic-internal evidence;
- no duplicate level-two headings in internal records;
- no auditor-authored commentary in internal records;
- inventory joins and NEURALIS facts remain aligned;
- the PBC request is absent;
- public-reference rights and provenance remain documented in `FRAMEWORK_SOURCE_PROVENANCE.md` and `original_public_sources/README.md`.
