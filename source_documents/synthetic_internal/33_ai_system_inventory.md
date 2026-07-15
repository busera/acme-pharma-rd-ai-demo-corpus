# ACME Pharma R&D AI system inventory extract

**Record owner:** R&D Digital Office, Enterprise Architecture
**Approver:** Enterprise AI Governance Office
**Status:** Controlled inventory extract
**Effective or as-of date:** 30 June 2026
**Review cycle:** Monthly

## Inventory purpose

The AI system inventory records the technical AI solutions used or planned in R&D. It is maintained by Enterprise Architecture with input from the Enterprise AI Governance Office, R&D Digital Office, Security, R&D Data Council, and system owners. The inventory must reconcile to business use cases, supplier records, cloud assets, model lifecycle documentation, and retirement plans.

## System inventory extract

| System ID | AI system | Hosting / supplier model | Status | Use case | Data class | GxP mapping | Pending action |
|---|---|---|---|---|---|---|---|
| SYS-AI-001 | Knowledge Search Assistant | ACME workspace; approved model endpoint | Operational | UC-RD-001 | Public scientific information | Not GxP | Source-quality monitoring limited |
| SYS-AI-002 | R&D Insight Workspace | ACME cloud tenant with vendor support | Controlled pilot | UC-RD-002 | Restricted research information | Boundary not triggered | Support access review not consistently evidenced |
| SYS-AI-003 | Project NEURALIS Assistant | ACME tenant; HelixBridge Analytics co-development support | Controlled development | UC-RD-003 | Public scientific information; Restricted research information | Pending GxP Boundary Review | Derived-artifact ownership and supplier support access remain open |
| SYS-AI-004 | Candidate Evidence Ranker | ACME-built pipeline with external components | Controlled pilot | UC-RD-004 | Restricted research information | Boundary not triggered | Portfolio decision traceability weak |
| SYS-AI-005 | Lab Record Drafting Assistant | Proposed vendor-hosted workflow | On hold | UC-RD-005 | GxP or submission-support information | GxP boundary triggered | Data integrity and assurance approach unresolved |
| SYS-AI-006 | Patent Landscape Copilot | External SaaS; ACME restricted tenant | Controlled development | UC-RD-006 | Public scientific information; Restricted research information | Not GxP | Privilege, IP reuse, and supplier training terms unresolved |
| SYS-AI-007 | Regulatory Drafting Support | Supplier not selected | Proposed only | UC-RD-007 | GxP or submission-support information | GxP boundary triggered | No drafting or submission use approved |
| SYS-AI-008 | Partner Intelligence Feed | Supplier-managed feed | Operational | UC-RD-009 | Public scientific information; Internal research information | Not GxP | Vendor change notification and evaluation evidence thin |
| SYS-AI-009 | External General AI Tools | Unapproved external tools | Unofficial | UC-RD-010 | Unknown | Not assessed | Shadow use remains unofficial; no formal monitoring |

## System lifecycle fields expected but incomplete

- Model or service version.
- Intended-use statement linked to each use case.
- Data-flow diagram and highest data class.
- Supplier and subprocessor list.
- Model card or equivalent system description.
- Evaluation and acceptance evidence.
- Change-control owner and release history.
- Monitoring plan and incident categories.
- Retirement and deletion procedure.

## Reconciliation rules

1. Every approved use case must link to a documented supporting AI system before release.
2. Cloud and procurement records must be reconciled monthly to identify systems awaiting AI classification.
3. Vendor-hosted tools must record prompts, outputs, embeddings, reviewer feedback, telemetry, and support access where those artifacts exist.
4. A move from public to restricted data requires a new intended-use and data-classification decision.
5. Reported shadow use is recorded as an unofficial system entry until it is stopped, replaced, or approved.

## System inventory fields

The system inventory records platform name, system owner, business owner, lifecycle state, model endpoint, hosting pattern, data stores, access model, supplier role, highest approved data class, GxP boundary, monitoring owner, and linked use cases. It also records whether the system stores source documents, extracted text, embeddings, prompts, outputs, feedback, telemetry, and system logs.

The inventory distinguishes approved systems from systems in development and external tools reported through survey or procurement review. A system can be approved for one data class and prohibited for another. Approval is therefore tied to intended use and data boundary, not only to the tool name.

## Control use

Governance uses the system inventory to trigger access reviews, model-change assessments, supplier reviews, retention checks, and incident response coverage. The inventory should reconcile to cloud resources, identity groups, procurement records, and use-case records. If a cloud workspace exists but no system record exists, the governance inventory is incomplete. If a system record exists but no current use case is linked, the system may be orphaned or awaiting retirement.
