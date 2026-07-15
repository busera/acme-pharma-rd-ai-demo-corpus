# Validation Plan for R&D AI Pilot

**Record owner:** NEURALIS Assurance Lead
**Approver:** Translational Medicine Business Owner
**Status:** Version 0.6, approved for execution
**Effective or as-of date:** 18 June 2026
**Review cycle:** Each release candidate

## Validation objective

The pilot validation does not prove scientific correctness. It tests whether the workflow produces useful, traceable, and reviewable suggestions under controlled conditions.

## Test categories

- Retrieval relevance: does the system find the right documents and passages?
- Context handling: does it consider broader source context rather than isolated snippets?
- Citation quality: are references specific and reviewable?
- Limitation recognition: does it state uncertainty and missing evidence?
- Safety boundaries: does it refuse or flag requests that involve restricted data or unapproved use?
- Reviewer usability: can scientists identify what was used and why?

## Acceptance criteria

Acceptance criteria are qualitative and quantitative but are not listed here as thresholds. The important planning point is that acceptance criteria must exist before expansion beyond the sandbox.

## Residual risk

Even a validated pilot may create overreliance risk if users treat confident wording as scientific evidence.

## Validation and assurance approach

The validation plan uses a risk-based assurance model. For exploratory literature support, evidence focuses on intended use, user training, source traceability, and output review. For workflows that may affect GxP or submission-support records, the plan requires a stronger package: requirements, risk assessment, test cases, traceability matrix, audit trail review, access-control evidence, change-control procedure, and periodic review.

## Reference expectations considered

The plan aligns with three public expectation families: FDA's risk-based computer software assurance direction for production and quality-system software, FDA Part 11 principles for electronic records and signatures where predicate records are involved, and GAMP 5's fit-for-intended-use, supplier involvement, critical thinking, data-integrity, cloud, and AI/ML lifecycle themes.

## Test scenarios

1. Public literature-only summary with correct source citations.
2. Restricted research information research note blocked from unapproved external processing.
3. Experiment-design suggestion requiring scientist approval before use.
4. Lab-note synthesis request that must not overwrite the original record.
5. Retrieval miss where contradictory evidence exists in a different source.
6. Supplier support access to a failed job containing restricted content.
7. Changed model or retrieval configuration requiring regression testing.

## Assurance approach

The validation plan uses a risk-based assurance approach rather than one uniform validation package for every AI use case. Productivity support using public information requires documented intended use, user guidance, and basic output review. Internal research data use requires security, privacy, legal/IP, data-flow, access, and output-review evidence. GxP-adjacent or submission-support use requires a stronger fit-for-intended-use rationale, traceability, change control, audit trail expectations, and review of how outputs enter controlled records.

The plan defines test categories: source retrieval accuracy, output grounding, contradiction handling, uncertainty labeling, human-review workflow, access control, logging, retention, deletion, and model-change impact. It also requires negative tests, such as asking the assistant to produce unsupported conclusions, use restricted data in an unapproved workspace, or treat draft output as final evidence.

## Evidence package

The expected evidence package includes intended-use statement, risk classification, data-flow record, test scripts or evaluation examples, reviewer scoring, defect log, release approval, monitoring plan, training record, and change-control procedure. For supplier co-development, the package must also include contract clauses, support-access rules, subprocessor evidence, no-training commitments, and exit/deletion requirements.
