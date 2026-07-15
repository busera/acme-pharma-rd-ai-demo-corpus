# ACME Pharma R&D AI Audit Planning Demo Corpus

This repository contains a curated public demo corpus for an article about AI-assisted audit planning in pharmaceutical R&D.

ACME Pharma is an obviously fake company name. The internal-looking documents are fabricated for demonstration and training purposes. They are not copied from, derived from, or intended to resemble any real pharmaceutical company, employee, supplier, internal system, audit identifier, or confidential engagement.

## What is included

- `source_documents/00_meta/` — central source-status statement and engagement metadata for the demo scenario.
- `source_documents/public_references/` — attributed public-source summaries and bounded excerpts used to ground realistic AI, GxP, data, privacy, third-party, and governance topics.
- `source_documents/synthetic_internal/` — ACME Pharma internal-looking R&D AI evidence documents for audit-planning demonstration.
- `original_public_sources/` — 13 exact external originals whose official reuse terms support redistribution; kept outside the scanner root to avoid duplicate weighting.
- `scripts/prepare_corpus.py` — verifies source hygiene, downloads seven additional current official sources with a drift receipt, and prepares summary or expanded-source inputs.
- `AGENTS.md` — operating instructions for AI agents preparing a clean APM/AWP input.
- `SOURCE_MAP.md` — file-level navigation map for the corpus.
- `FRAMEWORK_SOURCE_PROVENANCE.md` — authority, version, official URL, representation, and acquisition hashes for the 20 external framework sources reviewed for the corpus.
- `example_outputs/` — curated demonstration output generated from the corpus. The included APM extract is reduced to 5 selected risks out of 27 candidate risks from the source run.
- `article_assets/` — flattened PNG visuals used in the companion Medium article. These are public-safe article-support images, not implementation screenshots or raw audit outputs.

Current summary-corpus count: 55 Markdown files.

- Meta/source-status files: 2
- Public-reference files: 21
- ACME internal-looking evidence files: 32

## Development independence and overfitting boundary

This synthetic document corpus was not used during development of the AI-assisted audit-planning workflow. It was created as a separate public demonstration pack so the example could be run against evidence the workflow had not been tuned on.

That separation is intentional: it reduces the risk that the published demo reflects overfitting to a known document set, hard-coded examples, or source-specific prompt tuning. The corpus should therefore be treated as a fresh evaluation-style demonstration input, not as training material for the workflow itself.

Files in `source_documents/public_references/` and `source_documents/synthetic_internal/` intentionally omit pipeline-generated YAML frontmatter. Prior-run classifications, ratings, generated facts, and generated summaries are not source evidence and could pre-bias later intake. Authority, status, and applicability information is kept in the human-readable record body and the repository-level provenance inventory instead.

## What is intentionally excluded

This public package excludes runtime and local working artifacts: logs, raw generated APM output folders, state/cache folders, local configuration, local machine paths, AI runtime implementation details, graph refresh reports, downloaded publisher-restricted originals, and private vault context.

The repository is meant to publish the curated corpus, selected public demonstration extracts, and article-support visuals, not the broader working folder used to create or process it.

## How to use this corpus

Use it as a safe example set for:

- demonstrating audit-planning evidence intake;
- discussing AI governance, GxP, data, privacy, third-party, and R&D risks;
- creating public article visuals or examples without exposing real audit material;
- inspecting a short, curated generated-output extract without publishing the full raw APM run.

Use `AGENTS.md` and `scripts/prepare_corpus.py` to create either the stable 55-file summary corpus or an expanded 54-file input containing 32 internal records, 2 meta records, and 20 current official originals. The expanded mode excludes the 21 public-reference summaries so external authorities are not double-counted.

Do not use it to represent real company practices, make compliance claims, provide legal/regulatory/validation/audit assurance, or benchmark actual pharmaceutical companies.

## Public-source grounding

The corpus uses realistic themes informed by public materials from regulators, standards bodies, and security/governance sources, including FDA, EMA/HMA, eCFR, MHRA, ISPE/GAMP public summaries, NIST AI RMF, OECD AI-in-science and GLP data-integrity publications, OWASP LLM risk guidance, and cloud-provider security/privacy and ML architecture guidance.

Public-reference files summarize why each source matters for an AI-in-R&D audit-planning scenario and include bounded, attributed excerpts where useful. They are not a substitute for reading the original sources. `FRAMEWORK_SOURCE_PROVENANCE.md` identifies the exact acquired authorities and hashes used to prepare the records.

External references are planning inputs, not engagement evidence. They can identify candidate criteria and questions, but they cannot establish applicability, implementation, occurrence, control design, or operating effectiveness. Draft, advisory, vendor, and framework material must not be presented as binding law.

## Demo output extract

`example_outputs/ACME_Pharma_RnD_AI_APM_demo_output_5_risks.md` is a curated generated-output example. It is reduced to 5 selected risks out of 27 candidate risks identified in the generated run, and includes multiple APM areas: executive summary, engagement context, organizational context, risk universe, risk/control matrix, scope rationale, engagement objectives, work-program rows, logistics, and selected PBC/evidence requests.

This extract is included to show the type of planning output the corpus can support across more than one APM chapter. It is not a complete APM, not audit assurance, and not a production methodology.

The extract predates the July 2026 addition of six framework-reference records and was generated from the earlier 50-file corpus. It is retained as a reduced historical example; future runs should use a corpus prepared from the current repository and must not represent this extract as output from either current preparation mode.

## Source-status statement

Read `source_documents/00_meta/DEMO_SOURCE_STATEMENT.md` before reusing or citing the corpus. It defines the scope, purpose, public-source basis, and limitations of the demo pack.

## Reuse boundary

Use for demonstration, education, and article-support purposes only. Keep the ACME framing and central source-status statement with any reuse.
