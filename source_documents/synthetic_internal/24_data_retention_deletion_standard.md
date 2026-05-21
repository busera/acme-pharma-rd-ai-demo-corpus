---
title: Data Retention and Deletion Standard for AI Pilots
doc_type: standard
owner: Information Governance
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 24_data_retention_deletion_standard.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: Data Retention and Deletion Standard for AI Pilots. scenario: AI in
  Research and Development planning evidence.'
Summary: 'title: Data Retention and Deletion Standard for AI Pilots. doc_type: standard.
  owner: Information Governance. status: draft. company: ACME Pharma. confidentiality:
  Internal. scenario: AI in Research and Development planning evidence. Data Retention
  and Deletion Standard for AI Pilots. Retention principles. AI pilot data should
  be retained only as long as needed for evaluation, traceability, security investigation,
  and legal obligations.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Data Retention and Deletion Standard for AI Pilots


## Retention principles

AI pilot data should be retained only as long as needed for evaluation, traceability, security investigation, and legal obligations. The standard covers source documents, normalized text, embeddings, prompts, outputs, logs, model evaluation cases, caches, and backups.

## Deletion expectations

At the end of a pilot, the product owner must confirm which artifacts are retained, deleted, anonymized, or transferred to production controls. Third-party providers must provide deletion evidence where contractually required.

## Special issue: embeddings and derived artifacts

Embeddings and evaluation examples may preserve sensitive meaning even when they do not contain readable source text. The standard treats them as derived artifacts that inherit the classification of the source unless a documented risk assessment says otherwise.

## Audit planning relevance

The audit should test whether deletion requirements cover the full artifact chain, not just original uploaded files.

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

The standard defines retention for source documents, extracted text, embeddings, prompts, outputs, reviewer feedback, telemetry, audit logs, support logs, and exported files. Source documents follow the governing research-record or collaboration-retention rule. Prompts and outputs inherit the classification and retention requirement of the highest-risk source material when they contain internal research context. Embeddings are treated as derived records requiring deletion when the source workspace is retired unless Legal or Quality requires retention.

For sandbox pilots, default retention is intentionally short unless outputs are copied into controlled records. For routine use, retention must be aligned to business record requirements and evidence needs. For GxP-adjacent activity, retention and audit trail expectations must be reviewed with Quality.

## Deletion evidence

Deletion evidence must include workspace closure, revoked access, deleted source copies, deleted embeddings, deleted outputs where permitted, supplier deletion attestation, subprocessor confirmation where applicable, and a retained-artifact list. The retained-artifact list explains what remains and why.

The audit should test whether deletion is technically possible and evidenced. Many AI platforms can delete visible files but leave logs, embeddings, backups, or telemetry. The standard requires these residual stores to be named, risk-assessed, and contractually addressed.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 24 data retention deletion standard would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
