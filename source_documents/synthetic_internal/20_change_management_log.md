---
title: Change Management Log for R&D AI Pilot
doc_type: change log
owner: R&D AI Product Owner
status: working
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 20_change_management_log.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: Change Management Log for R&D AI Pilot. scenario: AI in Research and
  Development planning evidence.'
Summary: 'title: Change Management Log for R&D AI Pilot. doc_type: change log. owner:
  R&D AI Product Owner. status: working. company: ACME Pharma. confidentiality: Internal.
  scenario: AI in Research and Development planning evidence. Change Management Log
  for R&D AI Pilot. Recent changes. Concern.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Change Management Log for R&D AI Pilot


## Recent changes

| Date | Change | Reason | Approval status |
|---|---|---|---|
| 2026-03-05 | Added public literature corpus | support pilot testing | approved |
| 2026-03-12 | Added internal research summaries | improve relevance | pending Legal review |
| 2026-03-18 | Enabled vendor configuration support | implementation issue | time-bound approval |
| 2026-03-22 | Modified retrieval settings | reduce irrelevant passages | technical approval only |
| 2026-03-29 | Added output review template | improve reviewer feedback | approved |

## Concern

Technical changes are logged, but the change process does not consistently identify whether a change affects legal, privacy, security, or scientific-integrity risk. For example, adding internal research summaries changes the data-risk profile more than the wording of the change entry suggests.

## Recent changes under review

| Change | Reason | Risk question |
|---|---|---|
| Added patent-search connector | Improve IP landscape support | Does connector terms-of-use permit the intended processing? |
| Updated retrieval weighting | Improve negative-evidence recall | Has regression testing shown no loss in source precision? |
| Enabled reviewer comments | Improve human review evidence | Are comments retained as controlled records or monitoring data? |
| Added external collaborator role | Support university partnership | Does access respect partner-data restrictions and exit obligations? |
| Expanded summary templates | Improve consistency | Are users mistaking templates for approved scientific conclusions? |

## Change-control gap

The log records technical changes but does not always state whether a change affects intended use, GxP classification, supplier obligations, or validation scope. Audit should test whether changes that look minor technically can still be material from an R&D governance perspective.

## Change categories

The change log tracks model endpoint changes, prompt-library updates, retrieval-source changes, user-interface changes, access-role changes, retention-setting changes, supplier subprocessor changes, and intended-use changes. Each change should identify whether re-evaluation is required. The log treats model upgrades as potentially material even where the application code is unchanged.

For R&D AI, a change can affect scientific interpretation without changing system availability. A new model may produce more confident language, different source selection, weaker uncertainty statements, or different ranking logic. Prompt-library changes may alter the boundary between drafting support and decision support. Retrieval-source changes may introduce outdated or unapproved records.

## Audit observations

The current log contains examples of technical changes but fewer examples of impact assessment. Several entries state "no user impact" without explaining whether output behavior was tested. The audit should sample changes and request evidence of regression examples, reviewer sign-off, updated training where needed, and communication to users.

The change log should also connect to the AI system inventory. If a system is listed as running, its model and configuration changes should be visible. If a project is in development, design changes should still be tracked when they affect evaluation evidence.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 20 change management log would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
