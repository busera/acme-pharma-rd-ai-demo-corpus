---
title: 'Model Card: Experiment Design Assistant'
doc_type: model card
owner: R&D AI Product Owner
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 11_model_card_experiment_design_assistant.md
IIA_Type: EVD
IIA_Type_Rational: The model card serves as documented evidence of the AI pilot's
  intended use, limitations, and human review requirements, directly supporting the
  audit's assessment of governance and human control.
Quality_Rating: M
Relevance_Score: H
Fact: The model card states the Experiment Design Assistant is not intended for autonomous
  experiment approval, safety-critical decisions without scientific review, regulatory
  claim drafting, or use with restricted human-subject or clinical data. A principal
  scientist must approve any experiment design that relies on AI-generated suggestions,
  and reviewer notes should identify accepted and rejected suggestions. The model
  may overstate weak evidence, miss negative results, confuse similar protocols, or
  create plausible but unsupported rationale. Evaluation results show literature-grounded
  suggestions are mostly met but weak when source documents use inconsistent assay
  names, negative evidence retrieval is only partially met, and scientist usability
  is mixed with senior scientists wanting clearer uncertainty labels. The document
  is marked as draft and internal to ACME Pharma.
Summary: 'This internal draft model card describes the Experiment Design Assistant,
  an AI tool that reviews proposed early research experiments and suggests missing
  controls, confounders, feasibility constraints, and evidence gaps. It is intended
  to challenge completeness of study plans, not to decide final design or approve
  protocols. The document explicitly lists prohibited uses, including autonomous experiment
  approval, safety-critical decisions without scientific review, regulatory claim
  drafting, and use with restricted data. Known limitations include overstating weak
  evidence, missing contradictory internal notes, and producing plausible controls
  without recognizing feasibility constraints. Human review is mandatory: a principal
  scientist must approve any design relying on AI suggestions, documenting accepted
  and rejected suggestions. Evaluation results are provided for literature-grounded
  suggestions, negative evidence retrieval, GxP boundary handling, and scientist usability,
  with mixed performance noted. The model card is owned by the R&D AI Product Owner
  and is in draft status, indicating it is a living governance artifact.'
Section_Context: Evidence artifact
IIA_Relevance_Explanation: The model card serves as documented evidence of the AI
  pilot's intended use, limitations, and human review requirements, directly supporting
  the audit's assessment of governance and human control.
IIA_Relevance: H
IIA_Confidence: M
Notes: 'Auto-derived categorization: The model card serves as documented evidence
  of the AI pilot''s intended use, limitations, and human review requirements, directly
  supporting the audit''s asse...'
---

# Model Card: Experiment Design Assistant


## Intended use

The assistant suggests experiment-planning considerations based on approved protocols, historical observations, and public scientific context. It is intended to challenge completeness, not to decide the final design.

## Not intended for

- Autonomous experiment approval.
- Safety-critical decisions without scientific review.
- Regulatory claim drafting without validated evidence.
- Use with restricted human-subject or clinical data.
- Use with unapproved third-party data.

## Known limitations

The model may overstate support from weak evidence, miss negative results, confuse similar protocols, or create plausible but unsupported rationale. It may also fail to detect whether a prior experiment was exploratory, failed, superseded, or not comparable.

## Human review

A principal scientist must approve any experiment design that relies on AI-generated suggestions. Reviewer notes should identify accepted suggestions, rejected suggestions, and follow-up questions.

## Intended use

The Experiment Design Assistant reviews proposed early research experiments and suggests missing controls, likely confounders, feasibility constraints, and source-evidence gaps. It is not approved to select final study design, approve protocols, replace peer review, or make a candidate advancement decision.

## Evaluation results snapshot

| Test set | Pass criterion | Latest result | Concern |
|---|---|---|---|
| Literature-grounded suggestions | At least one source link for each material claim | Mostly met | Weak when source documents use inconsistent assay names |
| Negative evidence retrieval | Flags contradictory or failed prior results | Partially met | Negative results are often buried in appendices or short lab notes |
| GxP boundary handling | Refuses to draft final controlled-record language | Met in test cases | Needs periodic regression testing |
| Scientist usability | Reviewer marks suggestion useful and not misleading | Mixed | Senior scientists want clearer uncertainty labels |

## Known limitations

The model can overstate weak evidence, miss contradictory internal notes, and produce plausible experimental controls without recognizing feasibility constraints. Output must be reviewed by the accountable scientist against primary sources.

## Intended use and limitations

The experiment design assistant is intended to challenge draft study plans by identifying missing controls, likely confounders, feasibility constraints, inconsistent assumptions, and unresolved prior evidence. It does not design an experiment independently and does not approve protocols. The accountable scientist remains responsible for reviewing primary evidence, accepting or rejecting suggestions, and documenting rationale where AI output materially influenced the design discussion.

The model card states that the assistant may use public literature, approved internal methods summaries, prior non-confidential experiment templates, and controlled project context where the workspace is approved for restricted research data. It must not use personal notebooks, unapproved collaboration files, partner-confidential data without contract confirmation, or GxP records unless the use case has passed the higher assurance route.

## Evaluation expectations

Evaluation examples should include strong and weak study plans, missing negative controls, ambiguous endpoints, conflicting literature, small sample-size rationale, and feasibility constraints. Reviewers should score whether the assistant identifies issues, cites source context, avoids unsupported conclusions, and distinguishes suggestions from evidence. The model card requires tracking false confidence, missed confounders, irrelevant suggestions, and invented citations.

Monitoring includes user feedback, periodic sample review, model-version changes, retrieval-source changes, and incidents where an output was copied into a decision document without appropriate review. The audit should verify whether this model card is connected to actual release and monitoring records.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 11 model card experiment design assistant would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.