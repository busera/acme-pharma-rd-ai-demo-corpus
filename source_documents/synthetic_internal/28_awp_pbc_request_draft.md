---
title: Draft PBC Request List for R&D AI Audit
doc_type: PBC draft
owner: Internal Audit
status: planning draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 28_awp_pbc_request_draft.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: Draft PBC Request List for R&D AI Audit. scenario: AI in Research and
  Development planning evidence.'
Summary: 'title: Draft PBC Request List for R&D AI Audit. doc_type: PBC draft. owner:
  Internal Audit. status: planning draft. company: ACME Pharma. confidentiality: Internal.
  scenario: AI in Research and Development planning evidence. Requested documents.
  R&D AI strategy and roadmap. AI use-case inventory and approval records.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Draft PBC Request List for R&D AI Audit


## Requested documents

1. R&D AI strategy and roadmap.
2. AI use-case inventory and approval records.
3. Data classification rules for R&D information.
4. Third-party contracts, SOWs, and data processing terms for AI vendors.
5. Legal/IP review of model co-development and no-training terms.
6. TPRM assessment and vendor due diligence evidence.
7. Cloud architecture diagram and security review.
8. Data-flow documentation including prompts, outputs, embeddings, logs, and retention.
9. Model cards, validation plans, and pilot acceptance criteria.
10. Access control matrix and recent access review.
11. Change log and production-readiness assessments.
12. Incident response procedures for AI data leakage.
13. Training material and completion evidence for pilot users.
14. Output review templates and sample completed reviews using approved sample material.

## Note

This is a planning draft. The final request list should be narrowed after discovery to avoid overburdening the auditee and to focus on the most relevant risks.

## Draft PBC request list by risk area

| Risk area | Evidence request |
|---|---|
| Governance | AI strategy, use-case register, R&D AI committee minutes, expansion criteria |
| GxP boundary | Intended-use assessments, GxP trigger decisions, Quality/Regulatory review records |
| Data governance | Data-classification standard, approved data sets, upload controls, privacy review |
| Third party | SOW, DPA, no-training clause, subprocessor list, support-access logs, deletion certificate template |
| Cloud/security | Architecture diagram, data-flow map, IAM matrix, logging design, vulnerability/security review |
| Model lifecycle | SOP, model card, evaluation results, change log, regression-test evidence |
| Human review | Output review templates, accepted/rejected output examples, reviewer training records |
| Data integrity | Record-retention rule, source traceability design, audit trail evidence, Part 11 assessment where applicable |
| Shadow AI | Survey results, exception reports, communication plan, approved-tool adoption metrics |

## PBC scoping note

The initial evidence request should not ask for every AI artifact across ACME Pharma. It should start with the top pilot use cases and then expand if inventory or shadow-use evidence suggests unmanaged activity outside the formal pilot.

## Evidence request rationale

The PBC request is structured to test whether AI governance exists in operating evidence rather than policy alone. Requests cover inventories, governance approvals, use-case intake forms, system records, data-flow diagrams, supplier contracts, access reports, model cards, validation evidence, monitoring reports, incident logs, training records, and selected output-review samples.

The request asks management to provide evidence for at least four use cases: one running use case, one pilot, one in-development co-developed project, and one reported shadow-AI scenario. This sample is designed to test lifecycle differences. A single mature pilot would not prove that early-stage projects and unofficial usage are controlled.

## Clarifications for auditees

The audit team should clarify that it is not asking for confidential scientific content unless needed for a controlled sample. For most tests, metadata, workflow evidence, governance records, redacted examples, and process artifacts should be enough. If primary research content is needed, the request should specify data-handling expectations and limit the population.

The PBC list should also ask for evidence of what does not exist. For example, if no GxP-adjacent AI use case is approved, management should provide the boundary assessment or decision record that supports that position.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 28 awp pbc request draft would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
