# AWS Security Considerations for Data in Generative AI

## Authority and status

- **Issuer:** Amazon Web Services
- **Source:** AWS Prescriptive Guidance, *Security considerations for data in generative AI*
- **Version:** Living page; initial publication recorded as 16 July 2025; acquired 13 July 2026
- **Status:** Vendor guidance; non-binding and not independent assurance
- **Official source:** <https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-considerations-gen-ai/security.html>

## Audit-planning relevance

The guidance highlights security and data risks across generative-AI workflows. For the synthetic ACME R&D scenario, it supports questions about:

- which data may enter prompts, training, fine-tuning, retrieval, memory, logs, and outputs;
- privacy, anonymization, masking, tokenization, encryption, and data classification;
- least-privilege retrieval and role-based access control;
- audit logging, real-time monitoring, and anomalous-access detection;
- hallucination, data poisoning, prompt injection, model inversion, and output filtering;
- human review for critical outputs;
- identity, memory isolation, tool permissions, lineage, and auditability for agentic systems.

## Selected source excerpts

> “A fundamental principle is to avoid exposing confidential data.”

> “A least-privilege access model is crucial for minimizing data exposure.”

> “organizations should implement comprehensive audit logging and real-time monitoring to track data access, transformations, and model interactions.”

> “enterprises must capture the outputs, the precise data flows, the tool invocations, and the model responses that lead to every decision.”

## Use boundary

This is vendor guidance, not a legal requirement and not evidence that ACME implemented any stated control. It identifies candidate security questions that must be tested against the actual architecture, contracts, data flows, configuration, and operating evidence. Consult the current official page before reliance.
