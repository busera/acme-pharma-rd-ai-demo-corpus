---
title: Acceptable Use Policy for AI in R&D
doc_type: policy
owner: AI Governance Office
status: approved
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 15_acceptable_use_policy.md
IIA_Type: GOV
IIA_Type_Rational: This document is an internal policy that defines permitted and
  prohibited uses of AI in R&D, establishing governance controls for AI pilots.
Quality_Rating: H
Relevance_Score: H
Fact: The policy permits researchers to use approved AI tools for summarizing public
  literature, drafting non-confidential outlines, comparing public methods, generating
  non-production code examples, and preparing expert review questions. It prohibits
  uploading confidential research data to unapproved AI services, using AI for final
  scientific, safety, regulatory, or portfolio decisions, processing human-subject
  or clinical data, uploading partner data without contractual permission, inferring
  trade secrets, and using AI-generated content in external submissions without review.
  Users must check source evidence, label AI-assisted content, retain review notes
  for decision-relevant outputs, and report suspected data leakage or incorrect output
  that influenced a decision. The policy does not yet define how to monitor compliance
  without excessive surveillance. It also states that prompts and outputs containing
  internal research context are company records, and deleting a chat window does not
  delete them.
Summary: The Acceptable Use Policy for AI in R&D, owned by the AI Governance Office,
  establishes rules for researchers using AI tools. It permits the use of approved
  AI tools for tasks such as public-literature summarization, drafting non-confidential
  outlines, comparing public methods, generating code examples for non-production
  analysis, and preparing questions for expert review. Prohibited activities include
  uploading confidential research data to unapproved AI services, using AI to make
  final scientific, safety, regulatory, or portfolio decisions, processing human-subject,
  clinical, or personal data, uploading partner data without contractual permission,
  and using AI-generated content in external submissions without review. Users are
  responsible for verifying source evidence, labeling AI-assisted content where required,
  retaining review notes for decision-relevant outputs, and reporting any suspected
  data leakage or incorrect output that influenced a decision. The policy also notes
  that prompts and outputs become company records when they contain internal research
  context, and users must not assume that deleting a chat window deletes the underlying
  data. An open issue is that the policy does not yet define how to monitor compliance
  without creating excessive surveillance of research work.
Section_Context: Governance framework
IIA_Relevance_Explanation: This document is an internal policy that defines permitted
  and prohibited uses of AI in R&D, establishing governance controls for AI pilots.
IIA_Relevance: H
IIA_Confidence: H
Notes: 'Auto-derived categorization: This document is an internal policy that defines
  permitted and prohibited uses of AI in R&D, establishing governance controls for
  AI pilots.'
---

# Acceptable Use Policy for AI in R&D


## Permitted uses

Researchers may use approved AI tools for public-literature summarization, drafting non-confidential outlines, comparing public methods, generating code examples for non-production analysis, and preparing questions for expert review.

## Prohibited uses without additional approval

- Uploading confidential research data to unapproved AI services.
- Using AI to make final scientific, safety, regulatory, or portfolio decisions.
- Processing human-subject, clinical, or personal data.
- Uploading partner data without contractual permission.
- Asking tools to infer trade-secret or competitor-confidential information.
- Using AI-generated content in external submissions without review.

## User responsibilities

Users must check source evidence, label AI-assisted content where required, retain review notes for decision-relevant outputs, and report suspected data leakage or incorrect output that influenced a decision.

## Open issue

The policy does not yet define how to monitor compliance without creating excessive surveillance of research work.

## Allowed and prohibited uses

Allowed uses include public-literature summarization, source comparison, drafting meeting-preparation notes, identifying open questions, and suggesting experiment-review prompts inside approved environments. Prohibited uses include uploading restricted R&D data to unapproved tools, using AI to approve research direction, bypassing peer review, generating final regulatory claims, replacing original lab records, or asking a vendor model to process partner data without contractual approval.

## User obligations

Users must confirm data class before upload, check source links, mark output disposition, disclose material AI assistance when output influences a review decision, and escalate suspected leakage, incorrect high-impact output, or use-case drift. Managers must not measure productivity in a way that pressures scientists to accept AI output without review.

## Allowed and prohibited use

The acceptable-use policy allows approved AI tools for summarizing public literature, comparing source documents, drafting non-final summaries, identifying open questions, and challenging study-design assumptions. It prohibits entering restricted research information into unapproved tools, using AI output as the sole basis for scientific decisions, creating regulatory claims without source review, uploading partner-confidential material without contractual clearance, or using personal accounts for company research work.

The policy requires users to treat prompts and outputs as company records when they contain internal research context. Users must not assume that deleting a chat window deletes prompts, files, embeddings, telemetry, or support logs. The policy also states that output copied into project documents must be traceable to reviewed source evidence.

## Practical examples for researchers

Allowed: asking an approved tool to summarize ten public papers and list contradictions, then reviewing the cited papers manually. Allowed with approval: asking a controlled workspace to compare internal study notes and identify missing controls. Not allowed: pasting unpublished assay results into a public assistant to draft a candidate-ranking memo. Not allowed: asking an external tool to rewrite partner-confidential protocol text before Legal confirms the collaboration terms.

The audit should test whether policy examples match actual researcher scenarios. A policy that sounds clear to governance teams may still fail if researchers cannot tell whether their data is restricted, whether a tool is approved, or whether output can be reused in decision material.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 15 acceptable use policy would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.