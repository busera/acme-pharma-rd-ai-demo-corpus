---
title: Legal and IP Review Questions for R&D AI
doc_type: legal questions
owner: Legal / IP Counsel
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 07_legal_ip_review_questions.md
IIA_Type: CTX
IIA_Type_Rational: The document provides context on legal and IP considerations for
  AI pilots, outlining questions that must be addressed to ensure legal review and
  governance, which aligns with the audit objective.
Quality_Rating: M
Relevance_Score: H
Fact: 'The document lists specific legal and IP review questions for AI-assisted R&D,
  including protectability of AI-generated hypotheses, trade secret risks from disclosing
  unpublished research to external models, vendor contract prohibitions on using confidential
  material for training, ownership of co-developed prompts and artifacts, reuse of
  know-how by third-party personnel, offboarding evidence requirements, and records
  retention for patent and regulatory integrity. It states that R&D and Internal Audit
  should not answer these questions independently; the expected control is escalation,
  documented legal advice, and explicit business risk acceptance. Legal review groups
  concerns into five areas: sending confidential information to AI, supplier reuse
  of ACME know-how, ownership of co-developed items, impact on inventorship/patentability,
  and separation of privileged legal analysis from general R&D AI workflows. Practical
  examples illustrate scenarios requiring documented answers on data use, retention,
  privilege, ownership, and human review. The review also considers whether AI processing
  creates derivative artifacts that could reveal ACME''s scientific direction, and
  distinguishes administrative, scientific, and other output types.'
Summary: 'This document, drafted by Legal/IP Counsel, presents a structured set of
  legal and intellectual property review questions for the use of AI in R&D at ACME
  Pharma. It begins with specific questions addressing the protectability of AI-generated
  outputs, trade secret implications of sharing unpublished research with external
  models, contractual prohibitions on vendor use of confidential data for training,
  ownership of co-developed prompts and other artifacts, reuse of know-how by third-party
  personnel, offboarding evidence, and records retention for patent and regulatory
  integrity. The document establishes a legal boundary, emphasizing that R&D and Internal
  Audit must escalate these questions to Legal rather than answering them independently,
  with the expected control being documented legal advice and business risk acceptance.
  The legal review focus is consolidated into five key questions: whether ACME confidential
  information can be sent to the AI environment, whether supplier personnel or systems
  can reuse ACME know-how, who owns co-developed prompts, workflows, evaluation sets,
  adapters, and embeddings, whether AI-assisted invention support affects inventorship
  or patentability review, and how privileged or confidential legal analysis is kept
  out of general R&D AI workflows. Practical examples are provided to test these questions,
  such as a scientist uploading an unpublished assay summary, a vendor engineer reviewing
  failed prompts, a patent analyst comparing internal hypotheses with public claims,
  and a regulatory scientist drafting response language from approved internal documents.
  Each example requires a documented answer covering data use, retention, privilege/confidentiality,
  output ownership, and required human review. The document further frames the legal
  issue as whether AI processing changes the confidentiality, ownership, or reuse
  profile of ACME research information, noting that prompts, embeddings, reviewer
  comments, evaluation sets, and generated outputs could create derivative artifacts
  that reveal ACME''s scientific direction even if original data is deleted. The IP
  team distinguishes three types of output, including administrative and scientific,
  to guide review. Overall, the document serves as a planning tool to ensure legal
  and IP risks are systematically addressed before expanding AI pilots beyond the
  sandbox.'
Section_Context: Strategic/operational context
IIA_Relevance_Explanation: The document provides context on legal and IP considerations
  for AI pilots, outlining questions that must be addressed to ensure legal review
  and governance, which aligns with the audit objective.
IIA_Relevance: H
IIA_Confidence: M
Notes: 'Auto-derived categorization: The document provides context on legal and IP
  considerations for AI pilots, outlining questions that must be addressed to ensure
  legal review and governance,...'
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