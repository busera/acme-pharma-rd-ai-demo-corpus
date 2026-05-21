---
title: 'Excerpt: AI Co-Development Statement of Work'
doc_type: contract excerpt
owner: Procurement / Legal
status: sample
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 05_vendor_copro_sow_excerpt.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: ''Excerpt: AI Co-Development Statement of Work''. scenario: AI in Research
  and Development planning evidence.'
Summary: 'title: ''Excerpt: AI Co-Development Statement of Work''. doc_type: contract
  excerpt. owner: Procurement / Legal. status: sample. company: ACME Pharma. confidentiality:
  Internal. scenario: AI in Research and Development planning evidence. Excerpt: AI
  Co-Development Statement of Work. Scope excerpt. The implementation partner will
  support the design of a prototype assistant for experiment planning and research-document
  synthesis.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Excerpt: AI Co-Development Statement of Work


## Scope excerpt

The implementation partner will support the design of a prototype assistant for experiment planning and research-document synthesis. The partner will configure retrieval workflows, assist with evaluation design, and support pilot users during controlled testing.

## Data-use language requiring clarification

The draft states that project materials may be used to improve solution performance. It does not clearly distinguish between improvement of the customer-specific solution and improvement of the vendor's general products or models. It also does not define whether prompts, embeddings, evaluation cases, and error examples are customer confidential information.

## Ownership language requiring clarification

The draft states that pre-existing vendor tools remain vendor property, while project-specific deliverables are customer property. It does not clearly classify co-developed model adapters, evaluation harnesses, prompt libraries, feature engineering decisions, or workflow design patterns.

## Audit planning relevance

This document is intentionally ambiguous. It should drive discovery questions around IP ownership, vendor training restrictions, data retention, subcontracting, and post-engagement use of know-how.

## Contract clauses under review

| Clause area | Current SOW wording gap | Audit concern |
|---|---|---|
| Training and improvement | SOW restricts model training on ACME data but is unclear on support telemetry and prompt analytics | Supplier may retain useful know-how without explicit approval |
| Derived artifacts | Work products are assigned to ACME, but embeddings, evaluation cases, model adapters, and reusable pipeline patterns are not named | Ownership and exit rights may be ambiguous |
| Subprocessors | Cloud hosting is named; specialist annotation and monitoring subcontractors are not fully listed | Data-flow map may be incomplete |
| Support access | Emergency support access is allowed but log review timing is not specified | Sensitive prompts or outputs may be viewed without timely review |
| Exit | Return/deletion is required for source data but not for derived artifacts and backups | Offboarding evidence may be insufficient |

## Minimum evidence expected

Audit should request the signed agreement, data processing addendum, AI-specific no-training language, subprocessor list, architecture annex, support-access procedure, change-notification obligations, deletion certificate template, and a worked example showing how ACME can retrieve or destroy derived artifacts at exit.

## NEURALIS-specific SOW issue

For Project NEURALIS, the SOW names source code and formal documentation as ACME-owned deliverables, but it does not clearly name prompts, retrieval configuration, embeddings, evaluation datasets, reviewer feedback, monitoring definitions, or reusable solution patterns. Legal/IP has asked Procurement to add an AI artifact schedule before pilot expansion.

## Commercial and delivery scope details

The statement of work covers a co-development initiative where ACME provides scientific requirements, evaluation examples, domain review, and selected research context while the supplier provides model orchestration, interface design, retrieval support, and technical implementation. The SOW states that outputs are draft research-support artifacts only and cannot be used as sole evidence for candidate advancement, protocol approval, regulatory claims, or quality decisions.

Deliverables include a prototype workspace, a retrieval configuration, a prompt and workflow library, evaluation reports, issue logs, reviewer feedback summaries, training material, and an exit package. The exit package must include deletion attestation, returned or destroyed data sets, a list of retained supplier artifacts, unresolved defects, and any reusable components that the supplier believes are not ACME-confidential. This retained-artifact list is a key audit point because the boundary between generic know-how and ACME-derived know-how is often unclear.

## Control clauses requiring follow-up

The SOW includes restrictions on model training and product improvement, but the wording has exceptions for aggregated telemetry and support diagnostics. It requires supplier personnel with support access to be approved, but it does not yet specify whether subcontractors may view prompts, outputs, embeddings, evaluation examples, or feedback comments. It describes encryption and access control, but it does not define audit-log review frequency or evidence retention.

The audit should compare the SOW to the technical architecture, data-flow description, and access-control matrix. If the SOW says the supplier cannot access restricted data but the support model allows vendor engineers to inspect logs that include prompts or generated summaries, the contractual control is weaker than it appears.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 05 vendor copro sow excerpt would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
