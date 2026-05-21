---
title: Legal and IP Review Questions for R&D AI
doc_type: legal questions
owner: Legal / IP Counsel
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 07_legal_ip_review_questions.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: Legal and IP Review Questions for R&D AI. scenario: AI in Research and
  Development planning evidence.'
Summary: 'title: Legal and IP Review Questions for R&D AI. doc_type: legal questions.
  owner: Legal / IP Counsel. status: draft. company: ACME Pharma. confidentiality:
  Internal. scenario: AI in Research and Development planning evidence. Legal and
  IP Review Questions for R&D AI. Questions for AI-assisted R&D work. Are AI-generated
  hypotheses, summaries, or candidate rankings protectable or usable in patent strategy?'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Legal and IP Review Questions for R&D AI


## Questions for AI-assisted R&D work

1. Are AI-generated hypotheses, summaries, or candidate rankings protectable or usable in patent strategy?
2. Could disclosure of unpublished research text to an external model provider affect trade secret protection?
3. Does the contract prohibit vendor use of confidential material for model training, evaluation, benchmarking, support, or product improvement?
4. Who owns co-developed prompts, evaluation cases, model adapters, embeddings, workflow documentation, and derived improvements?
5. Can third-party personnel reuse non-documentary know-how acquired during the engagement when working with competitors?
6. What offboarding evidence is required from external contributors?
7. What records must be retained to support patent, regulatory, or scientific integrity positions?

## Legal boundary

R&D and Internal Audit should not answer these questions independently. The expected control is escalation, documented advice, and explicit business risk acceptance where residual exposure remains.

## Legal/IP review focus

Legal has grouped the review into five questions: whether ACME confidential information can be sent to the AI environment; whether supplier personnel or systems can reuse ACME know-how; who owns co-developed prompts, workflows, evaluation sets, adapters, and embeddings; whether AI-assisted invention support affects inventorship or patentability review; and how privileged or confidential legal analysis is kept out of general R&D AI workflows.

## Practical examples to test

- A scientist uploads an unpublished assay summary and asks for alternative mechanisms.
- A vendor engineer reviews failed prompts and recommends reusable prompt changes.
- A patent analyst asks the model to compare internal target hypotheses with public claims.
- A regulatory scientist asks for draft response language based on approved internal source documents.

Each example needs a documented answer on data use, retention, privilege/confidentiality, output ownership, and required human review.

## Legal/IP issue framing

The legal review focuses on whether AI processing changes the confidentiality, ownership, or reuse profile of ACME research information. The main concern is not only disclosure of a document. It is also whether prompts, embeddings, reviewer comments, evaluation sets, and generated outputs create derivative artifacts that could reveal ACME scientific direction. The review asks whether a supplier could lawfully retain generalized patterns learned from ACME workflows even if the original data is deleted.

The IP team distinguishes three types of output. Administrative output includes summaries, meeting notes, and draft task lists. Scientific support output includes suggested controls, confounders, mechanism comparisons, and candidate-ranking rationale. Potentially protectable output includes new hypotheses, assay design alternatives, or language that could later appear in a patent, publication, or regulatory document. The third category requires tighter review because ownership and inventorship questions may arise.

## Contract questions still open

Open questions include whether the supplier may use ACME feedback to improve generic model performance, whether supplier staff can view unpublished research content during support, whether generated outputs are assigned to ACME, and whether jointly developed prompts or evaluation rubrics are deliverables. Legal also wants confirmation that no ACME data is used to train foundation models or benchmark tools for other customers.

The audit should verify that legal questions are translated into operational controls. A legal memo is not enough if the intake form, SOW, architecture, and access-control process do not enforce the agreed restrictions.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 07 legal ip review questions would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
