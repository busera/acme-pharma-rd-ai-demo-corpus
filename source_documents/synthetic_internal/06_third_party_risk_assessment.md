# Third Party Risk Assessment Summary

**Record owner:** Third Party Risk Management
**Approver:** Supplier Co-Development Review
**Status:** Conditional assessment
**Effective or as-of date:** 8 May 2026
**Review cycle:** Quarterly during controlled development

## Assessment scope

The assessment covers HelixBridge Analytics, its cloud-hosted implementation environment, the approved model endpoint, supplier support operations, subprocessors, incident-response obligations, and contractual data-use restrictions for Project NEURALIS.

The controlled-development scope includes public scientific information and selected restricted internal research summaries. It excludes GxP or submission-support information, personal or sensitive data, production operation, and regulatory drafting. Prompts may still expose unpublished hypotheses, target-selection rationale, assay anomalies, partner-confidential context, and early scientific judgments.

## Inherent risk view

| Risk area | Rating | Basis |
|---|---|---|
| Data confidentiality | High | Restricted R&D context may be processed by supplier-supported services |
| Supplier and subprocessor access | High | Support personnel may access prompts, outputs, telemetry, or logs |
| Data residency | Medium-high | Final hosting and backup locations require confirmation |
| Operational dependency | Medium | The project is not production-critical, but co-developed configuration may be difficult to replace |
| Exit and deletion | Medium-high | Derived artifacts, backups, and evaluation data require explicit treatment |

## Required supplier records

1. Current security whitepaper and assurance reports.
2. Data processing agreement and subprocessor list.
3. Contract terms covering model training, service improvement, benchmarking, telemetry, and retention.
4. Architecture and data-flow diagram, including backup and support paths.
5. Named-role access model for supplier personnel and emergency support.
6. Incident notification procedure.
7. Exit plan and deletion-attestation format for source and derived artifacts.

## Conditional approval actions

| Action | Owner | Target date | Status |
|---|---|---|---|
| Add no-training and no-product-improvement restrictions covering prompts, outputs, evaluation sets, and reviewer feedback | Legal/IP and Procurement | 30 June 2026 | In progress |
| Confirm cloud data flow, residency, backup, and subprocessor locations | Security and HelixBridge Analytics | 30 June 2026 | Open |
| Document approval, logging, review, and revocation of supplier support access | Third Party Risk Management and Security | 15 July 2026 | Open |
| Extend privacy screening to collaborators and coded subject-data edge cases | Privacy | 31 July 2026 | Open |
| Expand the exit plan to embeddings, cached prompts, outputs, monitoring logs, evaluation data, and backups | R&D Digital Office and HelixBridge Analytics | 31 July 2026 | Open |
| Define the boundary between ACME-derived implementation knowledge and reusable supplier know-how | Legal/IP | 31 July 2026 | Open |

## Residual risk decision

Residual risk remains medium-high. Controlled development may continue with public scientific information and selected restricted internal summaries while the actions above are tracked. Expansion of data, users, supplier access, intended use, or lifecycle status requires a refreshed assessment and Supplier Co-Development Review approval.
