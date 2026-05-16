---
title: ACME Pharma R&D AI use-case inventory extract
company: ACME Pharma
doc_type: inventory extract
owner: Enterprise AI Governance Office / R&D Digital Office
status: working
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 32_ai_use_case_inventory.md
IIA_Type: EVD
IIA_Type_Rational: This inventory extract provides factual evidence of AI use cases,
  their status, and identified governance gaps, directly supporting the audit objective
  to assess governance and control before expansion.
Quality_Rating: H
Relevance_Score: H
Fact: The inventory lists nine AI use cases across R&D, with statuses including Running,
  Running pilot, In development, Proposed, and On hold. Each entry identifies a key
  governance gap, such as inconsistent citation review evidence for UC-RD-001, weak
  upload controls for UC-RD-002, a pending GxP boundary decision for UC-RD-003, and
  incomplete Part 11 assessment for UC-RD-005. Several use cases involve high decision
  impact and GxP relevance, including lab-note synthesis (UC-RD-005) and regulatory
  response drafting (UC-RD-007). The inventory is jointly owned by the Enterprise
  AI Governance Office and R&D Digital Office, indicating a governance structure,
  but the documented gaps suggest that governance, security, legal review, and traceability
  controls are not fully mature for many AI pilots.
Summary: The document is an extract from ACME Pharma's R&D AI use-case inventory,
  jointly owned by the Enterprise AI Governance Office and the R&D Digital Office.
  Its purpose is to record how R&D teams intend to use AI, requiring each entry to
  specify business owner, user population, intended use, data class, decision impact,
  external-party involvement, and supporting AI system. The extract presents nine
  use cases in a table, covering activities such as public literature triage, internal
  research-note summarization, experiment-design challenge, candidate prioritization,
  lab-note synthesis, patent landscape support, regulatory response drafting, biomarker-study
  feasibility summarization, and supplier literature monitoring. Statuses range from
  Running and Running pilot to In development, Proposed, and On hold. Data classes
  include public, restricted internal, GxP/study record data, and coded subject data,
  with decision impacts from low to high. Several use cases have high GxP or regulatory
  relevance, particularly those involving lab records, regulatory submissions, and
  clinical-adjacent data. Each use case is linked to a supporting AI system, though
  one is not yet assigned. Critically, the inventory highlights key governance gaps
  for every use case, such as inconsistent citation review, insufficient upload controls,
  pending GxP boundary decisions, lack of recorded review rationale, incomplete Part
  11 and data-integrity assessments, unclear privilege and reuse boundaries, lack
  of approval for submission-ready content, pending privacy and data-minimization
  reviews, and supplier terms needing review. This inventory serves as a central tracking
  tool that reveals both the scope of AI adoption and the specific governance deficiencies
  that must be addressed before expansion beyond sandbox environments.
Section_Context: Evidence artifact
IIA_Relevance_Explanation: This inventory extract provides factual evidence of AI
  use cases, their status, and identified governance gaps, directly supporting the
  audit objective to assess governance and control before expansion.
IIA_Relevance: H
IIA_Confidence: H
Notes: 'Auto-derived categorization: This inventory extract provides factual evidence
  of AI use cases, their status, and identified governance gaps, directly supporting
  the audit objective to as...'
---

# ACME Pharma R&D AI use-case inventory extract

## Inventory purpose

The use-case inventory records how R&D teams intend to use AI. It is owned jointly by the Enterprise AI Governance Office and the R&D Digital Office. Each entry must identify a business owner, user population, intended use, data class, decision impact, external-party involvement, and the AI system or systems that support the use case.

## Inventory extract

| Use case ID | Use case | Business owner | Status | Data class | Decision impact | GxP / regulated relevance | Supporting AI system | Key governance gap |
|---|---|---|---|---|---|---|---|---|
| UC-RD-001 | Public literature triage | Scientific Knowledge Management | Running | Public | Low | Low | SYS-AI-001 Knowledge Search Assistant | Citation review evidence inconsistent |
| UC-RD-002 | Internal research-note summarization | Discovery Research | Running pilot | Restricted internal | Medium | Possible downstream relevance | SYS-AI-002 R&D Insight Workspace | Upload controls need stronger evidence |
| UC-RD-003 | Experiment-design challenge | Translational Medicine | In development | Public plus selected internal summaries | Medium-high | Potential protocol-design influence | SYS-AI-003 Project NEURALIS Assistant | GxP boundary decision pending |
| UC-RD-004 | Candidate prioritization support | Research Portfolio Board | Running pilot | Restricted research | High | May influence portfolio governance | SYS-AI-004 Candidate Evidence Ranker | Review rationale not consistently recorded |
| UC-RD-005 | Lab-note synthesis | Preclinical Safety | On hold | GxP / study record data | High | High | SYS-AI-005 Lab Record Drafting Assistant | Part 11 and data-integrity assessment not complete |
| UC-RD-006 | Patent landscape support | Legal/IP and Discovery Research | In development | Public patents plus confidential invention notes | Medium-high | Low GxP, high IP relevance | SYS-AI-006 Patent Landscape Copilot | Privilege and reuse boundaries unclear |
| UC-RD-007 | Regulatory response outline drafting | Regulatory Science | Proposed | Approved source documents | High | High if used for submission content | SYS-AI-007 Regulatory Drafting Support | Not approved for submission-ready content |
| UC-RD-008 | Biomarker-study feasibility summarization | Translational Medicine | Proposed | Coded subject and study feasibility data | High | Clinical-adjacent privacy and regulatory relevance | Not assigned | Privacy and data-minimization review pending |
| UC-RD-009 | Supplier literature-monitoring feed | External Innovation | Running | Public plus partner watchlist | Low-medium | Low | SYS-AI-008 Partner Intelligence Feed | Supplier change and data-use terms need review |
| UC-RD-010 | Research meeting preparation assistant | Multiple R&D functions | Running unofficially | Unknown | Low to medium | Unknown | Unapproved external tools reported | Shadow AI; inventory incomplete |

## Status definitions

| Status | Meaning |
|---|---|
| Running | Available to users in an approved environment |
| Running pilot | Available to a restricted pilot group with active monitoring |
| In development | Build or configuration work underway; not released for routine use |
| Proposed | Idea accepted into intake but not yet built or approved |
| On hold | Blocked by risk, compliance, funding, or technical dependency |
| Running unofficially | Evidence suggests use outside the approved inventory |

## Audit observations from inventory review

- The inventory is useful, but it is not yet complete enough to prove AI use is controlled across R&D.
- Status labels are not always matched to evidence. For example, a use case may be marked as running pilot without current monitoring results.
- GxP relevance is often marked low when the immediate activity is exploratory, even though outputs may later influence protocol, study, or submission-support decisions.
- Supplier involvement is under-recorded at the use-case level when the underlying AI system is vendor-hosted.
- The inventory needs a reconciliation control against procurement, cloud, expense, browser extension, and user-survey data to identify shadow AI.

## Inventory reconciliation notes

The use-case inventory now distinguishes the business activity from the supporting system. For example, literature triage and experiment-design challenge may run on the same platform but have different decision impact, data classes, user populations, and review expectations. Conversely, one use case may use several systems: document repository, retrieval layer, model endpoint, workflow interface, and output archive.

The inventory includes running use cases, pilots, development projects, proposed use cases, on-hold items, and shadow-AI observations. Each entry should show owner, lifecycle state, decision impact, data class, external involvement, and whether the use case maps to a system inventory record. Entries without system mapping are not automatically invalid, but they require follow-up because technical risk cannot be assessed.

## Audit sampling approach

The audit should sample across states. A running use case tests monitoring and access review. A pilot tests gate evidence and time limits. A development project tests early governance. A proposed use case tests intake. A shadow-AI entry tests detection and remediation. The sample should include at least one external-party use case and one use case near the GxP or submission-support boundary.

The inventory should also record rejected or on-hold use cases. Rejections provide evidence that governance can say no or require redesign, which is often more persuasive than a list of approved tools.