# Procurement Intake Questionnaire for AI Vendors

**Record owner:** Procurement
**Approver:** Third Party Risk Management; Legal/IP; Security
**Status:** Questionnaire version 1.1
**Effective or as-of date:** 1 April 2026
**Review cycle:** Annual

## Required vendor responses

1. Describe all AI models, services, subcontractors, and regions involved.
2. Confirm whether customer data is used for training, fine-tuning, evaluation, debugging, support, product improvement, or benchmarking.
3. Describe tenant segregation, encryption, access logging, and support access controls.
4. State retention periods for prompts, outputs, uploaded documents, embeddings, logs, and backups.
5. Explain how customer data and derived artifacts are returned or deleted at exit.
6. Provide independent assurance reports, security documentation, and incident-notification commitments.
7. Explain IP ownership for co-developed artifacts.
8. Describe how model changes are communicated.

## Open action

The questionnaire asks the right questions, but there is not yet a clear scoring model or decision threshold for R&D-sensitive data.

## Procurement questions added for AI vendors

- Will the supplier use customer prompts, outputs, embeddings, evaluation cases, telemetry, or support tickets for model training, product improvement, benchmarking, or service optimization?
- Which subprocessors can access source data, prompts, embeddings, logs, outputs, or backups?
- What deletion evidence is available for source data and derived artifacts?
- Can ACME Pharma disable retention of prompts and outputs outside the approved evidence store?
- How are model, retrieval, and guardrail changes communicated?
- What documentation can be reused for risk-based assurance under GAMP/CSA expectations?
- What contractual inspection rights exist for cloud controls, support access, incident response, and data residency?

## Current intake status

The current questionnaire is too IT-security heavy. It needs stronger R&D questions about scientific integrity, IP, GxP trigger management, source traceability, and exit from co-developed artifacts.

## Intake questions added for AI services

The procurement questionnaire asks whether the supplier will process prompts, source files, embeddings, outputs, reviewer feedback, telemetry, support logs, or evaluation examples. It asks whether any data may be used for model training, product improvement, benchmarking, abuse monitoring, or service diagnostics. It also asks for subprocessors, data residency, deletion evidence, support-access model, and incident notification timelines.

For co-development, the questionnaire asks who owns prompts, configurations, evaluation sets, model adaptations, workflow designs, and defect findings. It also asks whether supplier personnel will learn ACME-specific research methods or decision criteria during the engagement and how that knowledge may be reused.

## Intake timing requirement

The questionnaire is only effective if used early. Several R&D teams involve Procurement after technical scoping is already advanced, which means supplier assumptions may be embedded before risk review. The intake process should trigger Legal/IP, Privacy, Security, Quality, and AI Governance review based on data class and intended use.
