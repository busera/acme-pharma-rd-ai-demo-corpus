---
title: Model Development Lifecycle SOP for R&D AI
doc_type: SOP
owner: AI Governance Office
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 10_model_development_lifecycle_sop.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: Model Development Lifecycle SOP for R&D AI. scenario: AI in Research
  and Development planning evidence.'
Summary: 'title: Model Development Lifecycle SOP for R&D AI. doc_type: SOP. owner:
  AI Governance Office. status: draft. company: ACME Pharma. confidentiality: Internal.
  scenario: AI in Research and Development planning evidence. Model Development Lifecycle
  SOP for R&D AI. Lifecycle stages. Intake and use-case classification.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Model Development Lifecycle SOP for R&D AI


## Lifecycle stages

1. Intake and use-case classification.
2. Data suitability and rights review.
3. Threat and misuse analysis.
4. Prototype design in sandbox.
5. Evaluation design and acceptance criteria.
6. Pilot approval.
7. Human review and feedback capture.
8. Production-readiness assessment.
9. Monitoring and periodic reassessment.
10. Decommissioning or controlled expansion.

## Required artifacts

Each AI use case should maintain a use-case record, accountable owner, data classification, model or service description, data-flow diagram, validation plan, known limitations, human review procedure, third-party risk assessment, security review, and change log.

## R&D-specific additions

For research use, the record should also capture whether outputs influence hypothesis generation, candidate selection, experiment prioritization, regulatory evidence, patent decisions, or collaboration discussions.

## Audit planning relevance

The SOP gives an expected-control baseline. The audit can compare actual pilot documents to the required artifacts without claiming that the SOP itself is sufficient.

## Lifecycle stages

The SOP divides AI lifecycle work into intake, intended-use classification, data approval, model or workflow design, supplier/co-development review, evaluation-case design, test execution, release approval, monitoring, change control, periodic review, and retirement. It distinguishes exploratory AI tools from AI systems that support regulated or GxP-relevant activity.

## GxP trigger questions

A use case requires Quality assessment if model output is copied into a controlled record, supports a decision later used in a regulatory submission, changes acceptance criteria or experimental design, affects GxP data processing, or becomes part of a validated process. The SOP currently says this assessment is required, but it does not yet define who can make the final GxP classification when R&D, Quality, and Regulatory disagree.

## Lifecycle stages

The lifecycle SOP defines seven stages: intake, risk classification, design, development or configuration, evaluation, release, monitoring, and retirement. Intake captures the business problem, intended use, users, data class, supplier involvement, and decision impact. Risk classification determines whether the use case is productivity support, decision support, GxP-adjacent, or record-generating. Design defines allowed inputs, expected outputs, human review points, and evidence retention.

Development may involve prompt configuration, retrieval setup, workflow design, model selection, interface design, or supplier co-development. Evaluation must test output quality against realistic examples, not only technical availability. Release requires sign-off from business owner, system owner, security, privacy, legal/IP, and quality where applicable. Monitoring includes usage, incidents, model changes, user feedback, output-quality issues, and unapproved expansion.

## Change and retirement expectations

The SOP requires a change record when the model, retrieval corpus, prompt library, user group, intended use, data class, or supplier access changes materially. A model upgrade is not treated as a routine patch if it changes behavior for a decision-support workflow. Retirement must include user notification, data export or deletion, revoked access, archive of validation evidence, and confirmation that downstream records remain understandable.

The audit should test whether lifecycle gates are documented in project records and whether gate evidence is complete before use cases move to routine operation. Particular attention should be paid to pilots that keep running after the original test window closes.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 10 model development lifecycle sop would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
