# Excerpt: AI Co-Development Statement of Work

**Record owner:** R&D Digital Office
**Approver:** Procurement and Legal/IP
**Status:** Draft commercial schedule
**Effective or as-of date:** 22 April 2026
**Review cycle:** Before execution

## Scope excerpt

The implementation partner will support the design of a prototype assistant for experiment planning and research-document synthesis. The partner will configure retrieval workflows, assist with evaluation design, and support pilot users during controlled testing.

## Data-use language requiring clarification

The draft states that project materials may be used to improve solution performance. It does not clearly distinguish between improvement of the customer-specific solution and improvement of the vendor's general products or models. It also does not define whether prompts, embeddings, evaluation cases, and error examples are customer confidential information.

## Ownership language requiring clarification

The draft states that pre-existing vendor tools remain vendor property, while project-specific deliverables are customer property. It does not clearly classify co-developed model adapters, evaluation harnesses, prompt libraries, feature engineering decisions, or workflow design patterns.

## Contract clauses under review

|---|---|---|
| Training and improvement | SOW restricts model training on ACME data but is unclear on support telemetry and prompt analytics | Supplier may retain useful know-how without explicit approval |
| Derived artifacts | Work products are assigned to ACME, but embeddings, evaluation cases, model adapters, and reusable pipeline patterns are not named | Ownership and exit rights may be ambiguous |
| Subprocessors | Cloud hosting is named; specialist annotation and monitoring subcontractors are not fully listed | Data-flow map may be incomplete |
| Support access | Emergency support access is allowed but log review timing is not specified | Sensitive prompts or outputs may be viewed without timely review |
| Exit | Return/deletion is required for source data but not for derived artifacts and backups | Offboarding evidence may be insufficient |



## NEURALIS-specific commercial position

For Project NEURALIS, the SOW names source code and formal documentation as ACME-owned deliverables, but it does not clearly name prompts, retrieval configuration, embeddings, evaluation datasets, reviewer feedback, monitoring definitions, or reusable solution patterns. Legal/IP has asked Procurement to add an AI artifact schedule before pilot expansion.

## Commercial and delivery scope details

The statement of work covers a co-development initiative where ACME provides scientific requirements, evaluation examples, domain review, and selected research context while the supplier provides model orchestration, interface design, retrieval support, and technical implementation. The SOW states that outputs are draft research-support artifacts only and cannot be used as sole evidence for candidate advancement, protocol approval, regulatory claims, or quality decisions.

Deliverables include a prototype workspace, a retrieval configuration, a prompt and workflow library, evaluation reports, issue logs, reviewer feedback summaries, training material, and an exit package. The exit package must include deletion attestation, returned or destroyed data sets, a list of retained supplier artifacts, unresolved defects, and any reusable components that the supplier believes are not ACME-confidential. This retained-artifact list is an open commercial point because the boundary between generic know-how and ACME-derived know-how is not yet agreed.

## Control clauses requiring follow-up

The SOW includes restrictions on model training and product improvement, but the wording has exceptions for aggregated telemetry and support diagnostics. It requires supplier personnel with support access to be approved, but it does not yet specify whether subcontractors may view prompts, outputs, embeddings, evaluation examples, or feedback comments. It describes encryption and access control, but it does not define system-log review frequency or evidence retention.
