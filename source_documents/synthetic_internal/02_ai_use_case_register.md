---
title: R&D AI Intake and Exception Register
company: ACME Pharma
doc_type: working register
owner: R&D Digital Office
status: working
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 02_ai_use_case_register.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: R&D AI Intake and Exception Register. scenario: AI in Research and Development
  planning evidence.'
Summary: 'title: R&D AI Intake and Exception Register. company: ACME Pharma. doc_type:
  working register. owner: R&D Digital Office. status: working. confidentiality: Internal.
  scenario: AI in Research and Development planning evidence. R&D AI Intake and Exception
  Register. Purpose. This working register is not the formal enterprise AI use-case
  inventory.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# R&D AI Intake and Exception Register

## Purpose

This working register is not the formal enterprise AI use-case inventory. It is the R&D Digital Office intake log used to capture proposed AI ideas, early triage decisions, exceptions, and items that still need reconciliation into the formal use-case inventory. The formal inventory extract is maintained separately in `32_ai_use_case_inventory.md`; this register shows the messier front door before governance has cleaned and approved each item.

The distinction matters for audit planning. A controlled organization can have both an intake register and an inventory, but they must reconcile. The intake register should contain ideas, early pilots, incomplete submissions, shadow-AI reports, and rejected or parked requests. The formal inventory should contain governed use cases with owner, intended use, data class, supporting system, status, and monitoring expectations.

## Intake register extract

| Intake ID | Request / observation | Source | Requested user group | Data expected | Initial triage | Link to formal inventory | Open issue |
|---|---|---|---|---|---|---|---|
| INT-RD-026 | Literature review assistant for public papers and internal target notes | R&D Digital intake form | Discovery Biology | Public literature plus selected internal summaries | Accepted for sandbox | UC-RD-001 / UC-RD-002 | Need clearer split between public-only and restricted-data use |
| INT-RD-031 | Experiment-design challenge assistant | Translational Science workshop | Translational Medicine | Protocol drafts, assay constraints, historical study notes | Accepted for development | UC-RD-003 | Quality boundary decision pending before broader pilot |
| INT-RD-034 | Lab-note synthesis for preclinical studies | Lab Operations request | Preclinical Safety | Lab notebook exports, assay observations, deviations | Parked / on hold | UC-RD-005 | Part 11, audit-trail, and original-record protection unresolved |
| INT-RD-037 | Candidate prioritization support | Portfolio Board action | Research Portfolio | Target profiles, assay summaries, safety signals | Accepted for controlled pilot | UC-RD-004 | Review rationale and decision-log evidence inconsistent |
| INT-RD-041 | Patent landscape summarizer | IP counsel request | Legal/IP and Discovery | Public patents plus invention summaries | Accepted for development | UC-RD-006 | Privilege, reuse, and no-training terms need final sign-off |
| INT-RD-044 | Regulatory response drafting outline | Regulatory Science proposal | Regulatory Science | Approved source documents and question logs | Proposed only | UC-RD-007 | Not approved for submission-ready content |
| INT-RD-049 | Biomarker-study feasibility summarization | Translational Medicine request | Translational Medicine | Coded subject and feasibility data | Returned for redesign | UC-RD-008 | Privacy and data-minimization review pending |
| OBS-RD-011 | Public AI tool used for meeting preparation and literature summaries | Shadow-AI survey | Multiple R&D functions | Unknown; likely public plus internal context | Exception follow-up | UC-RD-010 | Inventory incomplete; user guidance and approved alternatives needed |
| OBS-RD-014 | Supplier-hosted literature feed expanded to partner watchlist | Procurement review | External Innovation | Public publications plus partner watchlist | Needs supplier review | UC-RD-009 | Supplier change control and data-use terms unclear |

## Triage fields

Each intake record should capture request source, business sponsor, user group, intended use, expected data class, decision impact, external-party involvement, likely system or platform, requested timeline, and whether the item is new, an expansion of an existing use case, or an exception. Records should not be closed merely because a tool already exists. A new use of an approved tool can still create a new risk if the data class, decision impact, supplier access, or GxP boundary changes.

The register deliberately includes shadow-AI observations and returned requests. Removing these items would make governance look cleaner but less realistic. For audit purposes, rejected, parked, and exception records are useful evidence because they show whether the intake process detects risk and can require redesign.

## Reconciliation requirement

The register must reconcile to the formal AI use-case inventory and AI system inventory at least monthly. Any item accepted for sandbox, development, pilot, or routine use should have a formal inventory link or a dated remediation owner. Any item involving a supplier should also link to procurement and third-party risk records. Any item involving restricted research data, coded subject data, partner-confidential material, GxP-adjacent records, or submission-support material should show the required Legal/IP, Privacy, Security, and Quality review status.

Open intake records should not be treated as approved use cases. The audit should test whether teams understand this distinction. A common failure mode is that a request moves from intake conversation to informal pilot before the formal inventory and system records are complete.

## Register quality observations

The intake register is useful because it captures early demand and exceptions, but it is not yet reliable as a control by itself. Several entries were opened through workshops, emails, or procurement reviews rather than a single intake route. Some records identify a business sponsor but not a technical system owner. Others describe external involvement only as a model provider, without stating whether the provider hosts prompts, stores embeddings, receives telemetry, or has support access.

The status language is also inconsistent. Terms such as sandbox, pilot, proposed, parked, returned for redesign, and exception follow-up are used by different teams. The R&D Digital Office plans to align these labels to formal lifecycle states so management can distinguish unapproved ideas from approved pilots.

## Audit testing implications

Audit planning should treat this register as a source of samples and reconciliation tests, not as final proof of completeness. A practical sample should include one accepted sandbox item, one in-development item, one parked or returned item, one supplier-linked item, and one shadow-AI observation. The audit should compare each sample to the formal use-case inventory, system inventory, project approvals, procurement records, access records, and monitoring evidence.

Strong evidence would show that the intake register creates a governance trail: request received, data and decision impact classified, required reviewers identified, formal inventory record created, system record linked, and approval decision recorded. Weak evidence would show only a list of ideas with no owner, no system mapping, and no follow-up.

## Known control risk

The main risk is not that two registers exist. The risk is that they drift. If R&D teams rely on the intake register while Enterprise AI Governance relies on the formal inventory, management may not know which AI activities are actually running, which systems are supporting them, and which items have unresolved data, supplier, or GxP questions. The audit should therefore include a reconciliation procedure between this working register, the formal use-case inventory, the AI system inventory, cloud resources, procurement records, and survey results.
