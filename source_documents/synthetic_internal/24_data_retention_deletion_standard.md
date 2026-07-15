# Data Retention and Deletion Standard for AI Pilots

**Record owner:** R&D Records Management
**Approver:** R&D Data Council and Quality and Regulatory Science
**Status:** Version 1.0, effective
**Effective or as-of date:** 1 June 2026
**Review cycle:** Annual

## Retention principles

AI pilot data should be retained only as long as needed for evaluation, traceability, security investigation, and legal obligations. The standard covers source documents, normalized text, embeddings, prompts, outputs, logs, model evaluation cases, caches, and backups.

## Deletion expectations

At the end of a pilot, the product owner must confirm which artifacts are retained, deleted, anonymized, or transferred to production controls. Third-party providers must provide deletion evidence where contractually required.

## Embeddings and derived artifacts

Embeddings and evaluation examples may preserve sensitive meaning even when they do not contain readable source text. Derived artifacts inherit the highest source classification until the data owner and R&D Data Council approve a documented downgrade decision.

## Retention model

| Data object | Default rule | Exception |
|---|---|---|
| Source document | Retain per source system and project record rules | Delete earlier if project owner withdraws approval |
| Extracted text | Align to source retention and deletion | Shorter retention for failed extraction tests |
| Embeddings/index entries | Treat as derived confidential data | Delete with source unless documented basis exists |
| Prompts and outputs | Retain for reviewability in approved workspace | Redact or minimize where payload logging is not needed |
| Review comments | Retain with output disposition | GxP-relevant review may require controlled-record handling |
| Supplier support artifacts | Ticket-bound retention with deletion certificate | Longer retention only for active incident investigation |

## Deletion evidence expected

Deletion evidence must cover source files, extracted text, embeddings, prompts, outputs, logs, caches, evaluation sets, backups where technically feasible, and supplier-held support artifacts. The current standard is clear on source files but less clear on derived artifacts.

## Retention categories

The standard defines retention for source documents, extracted text, embeddings, prompts, outputs, reviewer feedback, telemetry, system logs, support logs, and exported files. Source documents follow the governing research-record or collaboration-retention rule. Prompts and outputs inherit the classification and retention requirement of the highest-risk source material when they contain internal research context. Embeddings are treated as derived records requiring deletion when the source workspace is retired unless Legal or Quality requires retention.

For sandbox pilots, default retention is intentionally short unless outputs are copied into controlled records. For routine use, retention must be aligned to business record requirements and evidence needs. For GxP-adjacent activity, retention and audit trail expectations must be reviewed with Quality.

## Deletion evidence

Deletion evidence must include workspace closure, revoked access, deleted source copies, deleted embeddings, deleted outputs where permitted, supplier deletion attestation, subprocessor confirmation where applicable, and a retained-artifact list. The retained-artifact list explains what remains and why.
