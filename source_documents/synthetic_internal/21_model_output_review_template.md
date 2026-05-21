---
title: Model Output Review Template
doc_type: template
owner: R&D Quality
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 21_model_output_review_template.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'scenario: AI in Research and Development planning evidence. Reviewer decision:
  accept, reject, revise, escalate.'
Summary: 'title: Model Output Review Template. doc_type: template. owner: R&D Quality.
  status: draft. company: ACME Pharma. confidentiality: Internal. scenario: AI in
  Research and Development planning evidence. Model Output Review Template. Review
  fields. Request topic.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Model Output Review Template


## Review fields

- Request topic.
- Source documents used.
- Key model claims.
- Evidence supporting each claim.
- Evidence missing or contradicted.
- Reviewer decision: accept, reject, revise, escalate.
- Whether the output influenced research planning.
- Follow-up action owner.

## Reviewer guidance

Do not treat fluent writing as evidence. Check whether the output used current source material, captured uncertainty, distinguished public literature from internal findings, and avoided unsupported recommendations. If the output proposes experiment changes, a principal scientist must document the final decision.

## Planning relevance

This template supports the human-in-the-loop control, but the audit should verify whether it is actually used and whether reviewers have enough time and expertise to challenge outputs.

## Required review fields

The review template requires source adequacy, source diversity, evidence conflicts, uncertainty level, data class, intended use, whether output influenced a decision, reviewer edits, final disposition, and accountable reviewer sign-off. For candidate prioritization or experiment design, the reviewer must state whether any AI suggestion changed the planned next step.

## Review-quality concern

A checked box that says "reviewed" is not enough. The template should force reviewers to record why the output was accepted, edited, rejected, or escalated. For high-impact use cases, accepted output needs an evidence note linking the conclusion back to primary sources.

## Reviewer workflow

The review template requires the accountable scientist or qualified reviewer to check source relevance, factual accuracy, uncertainty, contradictory evidence, limitations, and decision impact. Reviewers must mark whether output is acceptable as a draft, acceptable after edits, rejected, or escalated for governance review. The template is not intended to create a bureaucratic sign-off for every low-risk summary, but it is required when output is reused in study design, candidate review, regulatory drafting, or governance material.

The reviewer must identify the source documents reviewed and note any missing primary evidence. If the output makes a claim that is not supported by the cited source, the reviewer must either remove the claim or add the correct source evidence. If the output identifies a risk, confounder, or contradiction, the reviewer records whether it changed the planned research action.

## Evidence value for audit

Completed templates can show whether human-in-the-loop control is real. Weak templates contain only "reviewed" with no source reference or decision rationale. Strong templates show what was checked, what was changed, what remained uncertain, and who accepted the scientific judgment.

The audit should sample review templates linked to high-impact outputs. It should compare AI output, reviewer comments, final decision material, and source evidence. The key test is whether review occurred before the output influenced the decision, not after.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 21 model output review template would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
