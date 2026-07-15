# R&D AI Intake and Exception Register

**Record owner:** R&D Digital Office
**Approver:** R&D AI Steering Committee
**Status:** Working register
**Effective or as-of date:** 30 June 2026
**Review cycle:** Monthly

## Purpose

This working register is not the formal enterprise AI use-case inventory. It is the R&D Digital Office intake log used to capture proposed AI ideas, early triage decisions, exceptions, and items that still need reconciliation into the formal use-case inventory. The formal inventory extract is maintained separately in `32_ai_use_case_inventory.md`; this register shows the messier front door before governance has cleaned and approved each item.


## Intake register extract

| Intake ID | Request or observation | Use case | Status | Data class | GxP mapping | System | Pending action |
|---|---|---|---|---|---|---|---|
| INT-RD-022 | Public literature triage | UC-RD-001 | Operational | Public scientific information | Not GxP | SYS-AI-001 | Citation review evidence inconsistent |
| INT-RD-026 | Internal research-note summarization | UC-RD-002 | Controlled pilot | Restricted research information | Boundary not triggered | SYS-AI-002 | Upload controls need stronger evidence |
| INT-RD-031 | Experiment-design challenge | UC-RD-003 | Controlled development | Public scientific information; Restricted research information | Pending GxP Boundary Review | SYS-AI-003 | Derived-artifact ownership and supplier support access remain open |
| INT-RD-037 | Candidate prioritization support | UC-RD-004 | Controlled pilot | Restricted research information | Boundary not triggered | SYS-AI-004 | Review rationale is not consistently recorded |
| INT-RD-034 | Lab-note synthesis | UC-RD-005 | On hold | GxP or submission-support information | GxP boundary triggered | SYS-AI-005 | Original-record protection and assurance approach unresolved |
| INT-RD-041 | Patent landscape support | UC-RD-006 | Controlled development | Public scientific information; Restricted research information | Not GxP | SYS-AI-006 | Privilege, reuse, and no-training terms need sign-off |
| INT-RD-044 | Regulatory response outline drafting | UC-RD-007 | Proposed only | GxP or submission-support information | GxP boundary triggered | SYS-AI-007 | No drafting or submission use approved |
| INT-RD-049 | Biomarker-study feasibility summarization | UC-RD-008 | Proposed | Personal or sensitive data | Pending GxP Boundary Review | Not assigned | Privacy and data-minimization review pending |
| INT-RD-052 | Supplier literature-monitoring feed | UC-RD-009 | Operational | Public scientific information; Internal research information | Not GxP | SYS-AI-008 | Supplier change control and data-use terms unclear |
| OBS-RD-011 | Research meeting preparation in external tools | UC-RD-010 | Unofficial | Unknown | Not assessed | SYS-AI-009 | Shadow use remains unofficial; inventory details are incomplete |

## Triage fields

Each intake record should capture request source, business sponsor, user group, intended use, expected data class, decision impact, external-party involvement, likely system or platform, requested timeline, and whether the item is new, an expansion of an existing use case, or an exception. Records should not be closed merely because a tool already exists. A new use of an approved tool can still create a new risk if the data class, decision impact, supplier access, or GxP boundary changes.


## Reconciliation requirement

The register must reconcile to the formal AI use-case inventory and AI system inventory at least monthly. Any item accepted for sandbox, development, pilot, or routine use should have a formal inventory link or a dated remediation owner. Any item involving a supplier should also link to procurement and third-party risk records. Any item involving restricted research data, coded subject data, partner-confidential material, GxP-adjacent records, or submission-support material should show the required Legal/IP, Privacy, Security, and Quality review status.


## Register maintenance actions

Several entries were opened through workshops, emails, or procurement reviews rather than the standard intake route. The R&D Digital Office is assigning technical system owners where only a business sponsor is recorded and expanding supplier fields to show hosting, prompt and embedding storage, telemetry, and support access.

Status labels from older entries, including sandbox, parked, and returned for redesign, will be mapped to the approved lifecycle states by 31 July 2026. New entries must use the controlled values shown in the formal use-case inventory.
