# ACME Pharma R&D AI Audit Planning Demo Corpus

This repository contains a curated public demo corpus for an article about AI-assisted audit planning in pharmaceutical R&D.

ACME Pharma is an obviously fake company name. The internal-looking documents are fabricated for demonstration and training purposes. They are not copied from, derived from, or intended to resemble any real pharmaceutical company, employee, supplier, internal system, audit identifier, or confidential engagement.

## What is included

- `source_documents/00_meta/` — central source-status statement and engagement metadata for the demo scenario.
- `source_documents/public_references/` — public-source summaries used to ground realistic AI, GxP, data, privacy, third-party, and governance topics.
- `source_documents/synthetic_internal/` — ACME Pharma internal-looking R&D AI evidence documents for audit-planning demonstration.
- `SOURCE_MAP.md` — file-level navigation map for the corpus.
- `example_outputs/` — curated demonstration output generated from the corpus. The included APM extract is reduced to 5 selected risks out of 27 candidate risks from the source run.

Current source-document count: 50 markdown files.

- Meta/source-status files: 2
- Public-reference files: 15
- ACME internal-looking evidence files: 33

## What is intentionally excluded

This public package excludes runtime and local working artifacts: logs, raw generated APM output folders, state/cache folders, configuration files, local machine paths, AI runtime implementation details, graph refresh reports, package manifests, and private vault context.

The repository is meant to publish the curated corpus and selected public demonstration extracts, not the broader working folder used to create or process it.

## How to use this corpus

Use it as a safe example set for:

- demonstrating audit-planning evidence intake;
- discussing AI governance, GxP, data, privacy, third-party, and R&D risks;
- creating public article visuals or examples without exposing real audit material;
- inspecting a short, curated generated-output extract without publishing the full raw APM run.

Do not use it to represent real company practices, make compliance claims, provide legal/regulatory/validation/audit assurance, or benchmark actual pharmaceutical companies.

## Public-source grounding

The corpus uses realistic themes informed by public materials from regulators, standards bodies, and security/governance sources, including FDA, EMA/HMA, MHRA, ISPE/GAMP public summaries, NIST AI RMF, OECD AI-in-science publications, OWASP LLM risk guidance, and cloud-provider security/privacy guidance.

Public-reference files summarize why each source matters for an AI-in-R&D audit-planning scenario. They are not a substitute for reading the original sources.

## Demo output extract

`example_outputs/ACME_Pharma_RnD_AI_APM_demo_output_5_risks.md` is a curated generated-output example. It is reduced to 5 selected risks out of 27 candidate risks identified in the generated run, and includes extracts for the risk universe, risk/control matrix, scope rationale, and work-program rows.

This extract is included to show the type of planning output the corpus can support. It is not a complete APM, not audit assurance, and not a production methodology.

## Source-status statement

Read `source_documents/00_meta/DEMO_SOURCE_STATEMENT.md` before reusing or citing the corpus. It defines the scope, purpose, public-source basis, and limitations of the demo pack.

## Reuse boundary

Use for demonstration, education, and article-support purposes only. Keep the ACME framing and central source-status statement with any reuse.
