---
title: Procurement Intake Questionnaire for AI Vendors
doc_type: questionnaire
owner: Procurement
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 23_procurement_intake_questionnaire.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: Procurement Intake Questionnaire for AI Vendors. scenario: AI in Research
  and Development planning evidence.'
Summary: 'title: Procurement Intake Questionnaire for AI Vendors. doc_type: questionnaire.
  owner: Procurement. status: draft. company: ACME Pharma. confidentiality: Internal.
  scenario: AI in Research and Development planning evidence. Procurement Intake Questionnaire
  for AI Vendors. Required vendor responses. Describe all AI models, services, subcontractors,
  and regions involved.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Procurement Intake Questionnaire for AI Vendors


## Required vendor responses

1. Describe all AI models, services, subcontractors, and regions involved.
2. Confirm whether customer data is used for training, fine-tuning, evaluation, debugging, support, product improvement, or benchmarking.
3. Describe tenant segregation, encryption, access logging, and support access controls.
4. State retention periods for prompts, outputs, uploaded documents, embeddings, logs, and backups.
5. Explain how customer data and derived artifacts are returned or deleted at exit.
6. Provide audit reports, security documentation, and incident-notification commitments.
7. Explain IP ownership for co-developed artifacts.
8. Describe how model changes are communicated.

## Gap

The questionnaire asks the right questions, but there is not yet a clear scoring model or decision threshold for R&D-sensitive data.

## Procurement questions added for AI vendors

- Will the supplier use customer prompts, outputs, embeddings, evaluation cases, telemetry, or support tickets for model training, product improvement, benchmarking, or service optimization?
- Which subprocessors can access source data, prompts, embeddings, logs, outputs, or backups?
- What deletion evidence is available for source data and derived artifacts?
- Can ACME Pharma disable retention of prompts and outputs outside the approved evidence store?
- How are model, retrieval, and guardrail changes communicated?
- What documentation can be reused for risk-based assurance under GAMP/CSA expectations?
- What audit rights exist for cloud controls, support access, incident response, and data residency?

## Procurement gap

The current questionnaire is too IT-security heavy. It needs stronger R&D questions about scientific integrity, IP, GxP trigger management, source traceability, and exit from co-developed artifacts.

## Intake questions added for AI services

The procurement questionnaire asks whether the supplier will process prompts, source files, embeddings, outputs, reviewer feedback, telemetry, support logs, or evaluation examples. It asks whether any data may be used for model training, product improvement, benchmarking, abuse monitoring, or service diagnostics. It also asks for subprocessors, data residency, deletion evidence, support-access model, and incident notification timelines.

For co-development, the questionnaire asks who owns prompts, configurations, evaluation sets, model adaptations, workflow designs, and defect findings. It also asks whether supplier personnel will learn ACME-specific research methods or decision criteria during the engagement and how that knowledge may be reused.

## Procurement control gap

The questionnaire is only effective if used early. Several R&D teams involve Procurement after technical scoping is already advanced, which means supplier assumptions may be embedded before risk review. The intake process should trigger Legal/IP, Privacy, Security, Quality, and AI Governance review based on data class and intended use.

The audit should select recent AI-related purchase requests and compare questionnaire answers to SOW language, architecture records, and actual project use. Inconsistencies are likely around telemetry, support access, and derived artifacts.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 23 procurement intake questionnaire would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
