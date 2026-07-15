# ACME Pharma R&D AI use-case inventory extract

**Record owner:** R&D Digital Office
**Approver:** R&D AI Steering Committee
**Status:** Controlled inventory extract
**Effective or as-of date:** 30 June 2026
**Review cycle:** Monthly

## Inventory purpose

The use-case inventory records how R&D teams intend to use AI. It is owned jointly by the Enterprise AI Governance Office and the R&D Digital Office. Each entry must identify a business owner, user population, intended use, data class, decision impact, external-party involvement, and the AI system or systems that support the use case.

## Inventory extract

| Use case ID | Use case | Business owner | Status | Data class | Decision impact | GxP / regulated relevance | Supporting AI system | Pending action |
|---|---|---|---|---|---|---|---|---|
| UC-RD-001 | Public literature triage | Scientific Knowledge Management | Operational | Public scientific information | Low | Not GxP | SYS-AI-001 Knowledge Search Assistant | Citation review evidence inconsistent |
| UC-RD-002 | Internal research-note summarization | Discovery Research | Controlled pilot | Restricted research information | Medium | Boundary not triggered | SYS-AI-002 R&D Insight Workspace | Upload controls need stronger evidence |
| UC-RD-003 | Experiment-design challenge | Translational Medicine | Controlled development | Public scientific information; Restricted research information | Medium-high | Pending GxP Boundary Review | SYS-AI-003 Project NEURALIS Assistant | Derived-artifact ownership and supplier support access remain open |
| UC-RD-004 | Candidate prioritization support | Research Portfolio Board | Controlled pilot | Restricted research information | High, advisory only | Boundary not triggered | SYS-AI-004 Candidate Evidence Ranker | Review rationale not consistently recorded |
| UC-RD-005 | Lab-note synthesis | Preclinical Safety | On hold | GxP or submission-support information | High | GxP boundary triggered | SYS-AI-005 Lab Record Drafting Assistant | Data-integrity and assurance approach not complete |
| UC-RD-006 | Patent landscape support | Legal/IP and Discovery Research | Controlled development | Public scientific information; Restricted research information | Medium-high | Not GxP | SYS-AI-006 Patent Landscape Copilot | Privilege and reuse boundaries unclear |
| UC-RD-007 | Regulatory response outline drafting | Regulatory Science | Proposed only | GxP or submission-support information | High | GxP boundary triggered | SYS-AI-007 Regulatory Drafting Support | No drafting or submission use approved |
| UC-RD-008 | Biomarker-study feasibility summarization | Translational Medicine | Proposed | Personal or sensitive data | High | Pending GxP Boundary Review | Not assigned | Privacy and data-minimization review pending |
| UC-RD-009 | Supplier literature-monitoring feed | External Innovation | Operational | Public scientific information; Internal research information | Low-medium | Not GxP | SYS-AI-008 Partner Intelligence Feed | Supplier change and data-use terms need review |
| UC-RD-010 | Research meeting preparation assistant | Multiple R&D functions | Unofficial | Unknown | Low to medium | Not assessed | SYS-AI-009 External General AI Tools | Shadow use remains unofficial and inventory details are incomplete |

## Status definitions

| Status | Meaning |
|---|---|
| Operational | Available to users in an approved environment |
| Controlled pilot | Available to a restricted pilot group with active monitoring |
| Controlled development | Build or configuration work underway; not released for routine use |
| Proposed / proposed only | Accepted into intake but not built or approved; proposed only prohibits activity beyond concept work |
| On hold | Blocked by risk, compliance, funding, or technical dependency |
| Unofficial | Reported use outside an approved environment |

## Inventory reconciliation notes

The use-case inventory now distinguishes the business activity from the supporting system. For example, literature triage and experiment-design challenge may run on the same platform but have different decision impact, data classes, user populations, and review expectations. Conversely, one use case may use several systems: document repository, retrieval layer, model endpoint, workflow interface, and output archive.

The inventory includes running use cases, pilots, development projects, proposed use cases, on-hold items, and shadow-AI observations. Each entry should show owner, lifecycle state, decision impact, data class, external involvement, and whether the use case maps to a system inventory record. Entries without system mapping are not automatically invalid, but they require follow-up because technical risk cannot be assessed.
