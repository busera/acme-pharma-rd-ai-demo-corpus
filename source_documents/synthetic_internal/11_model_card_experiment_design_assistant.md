# Model Card: Experiment Design Assistant

**Record owner:** NEURALIS Product Owner
**Approver:** Translational Medicine Business Owner
**Status:** Version 0.7, development record
**Effective or as-of date:** 12 June 2026
**Review cycle:** Each release candidate

## Not intended for

- Autonomous experiment approval.
- Safety-critical decisions without scientific review.
- Regulatory claim drafting without validated evidence.
- Use with restricted human-subject or clinical data.
- Use with unapproved third-party data.

## Human review

A principal scientist must approve any experiment design that relies on AI-generated suggestions. Reviewer notes should identify accepted suggestions, rejected suggestions, and follow-up questions.

## Intended use

The Experiment Design Assistant reviews proposed early research experiments and suggests missing controls, likely confounders, feasibility constraints, and source-evidence gaps. It is not approved to select final study design, approve protocols, replace peer review, or make a candidate advancement decision.

## Evaluation results snapshot

| Test set | Pass criterion | Latest result | Current limitation |
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
