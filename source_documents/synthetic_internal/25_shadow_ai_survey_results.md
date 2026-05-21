---
title: Shadow AI Survey Results in R&D
doc_type: survey summary
owner: R&D Digital Office
status: sample
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 25_shadow_ai_survey_results.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'scenario: AI in Research and Development planning evidence. A voluntary survey
  asked researchers how they use AI tools.'
Summary: 'title: Shadow AI Survey Results in R&D. doc_type: survey summary. owner:
  R&D Digital Office. status: sample. company: ACME Pharma. confidentiality: Internal.
  scenario: AI in Research and Development planning evidence. Shadow AI Survey Results
  in R&D. Survey summary. A voluntary survey asked researchers how they use AI tools.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Shadow AI Survey Results in R&D


## Survey summary

A voluntary survey asked researchers how they use AI tools. Responses suggest three patterns: approved enterprise tools for drafting and summarization, public tools for literature questions, and unapproved tools used experimentally for code, translation, and explaining methods.

## Key findings

- Some researchers do not know whether public AI tools retain prompts.
- Several users assume that public papers can always be pasted into any AI tool.
- A minority reported using AI to summarize internal meeting notes.
- Users want a safe tool for quick literature and protocol questions.
- Few users understand the difference between data processing and model training.

## Planning relevance

Shadow usage is not proof of control failure by itself, but it is a strong signal that inventory, training, approved-tool availability, and monitoring need attention.

## Survey results snapshot

The R&D Digital Office surveyed 480 employees across discovery, translational science, preclinical safety, regulatory science, and portfolio teams. Thirty-eight percent reported using at least one non-approved AI tool for public information. Nine percent reported uncertainty about whether internal project language had been pasted into an external tool. The most common reasons were faster literature summaries, easier meeting preparation, and frustration with slow approval of sanctioned tools.

## Control implication

A policy-only response is unlikely to work. The survey points to a demand signal: researchers need approved ways to summarize literature, compare sources, and challenge experiment assumptions. The audit should test whether approved tooling, training, and intake speed are realistic enough to reduce shadow use.

## Survey findings

The survey found that researchers use AI tools mainly for literature summaries, language polishing, code snippets, meeting-note cleanup, and first-pass protocol challenge. Most respondents said they avoid entering confidential information, but several were unsure whether internal abstracts, unpublished hypotheses, or partner-provided protocol text counted as confidential. Some users believed that removing compound names or project codes was enough to make content safe for public tools.

The survey also found that approved tools are viewed as slower and less flexible than public assistants. Teams described governance intake as unclear and said they did not know whether a small experiment required formal review. This creates a shadow-AI driver: users are not necessarily trying to bypass controls; they are solving immediate work problems where approved routes feel too slow.

## Audit interpretation

Survey results should be used as risk evidence, not as a final issue. The underlying risks are incomplete inventory, unclear user guidance, data-classification misunderstanding, and insufficient approved tooling. The audit should compare survey findings to access logs, training records, procurement requests, and help-desk questions.

A useful test is to ask teams to classify realistic examples: a public paper, an internal literature summary, an unpublished assay result, partner-confidential protocol language, and coded biomarker data. Classification inconsistency would support a control-design gap.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 25 shadow ai survey results would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
