# AWS Generative AI Security Scoping Matrix

## Authority and status

- **Issuer:** Amazon Web Services
- **Primary source:** *Securing generative AI: An introduction to the Generative AI Security Scoping Matrix*
- **Published:** 19 October 2023; acquired 15 July 2026
- **Status:** Vendor security framework; non-binding and not independent assurance
- **Official source:** <https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/>
- **Current companion page:** <https://aws.amazon.com/ai/security/generative-ai-scoping-matrix/>

## Audit-planning relevance

The matrix classifies generative-AI use cases by the organization’s ownership and control over the application, model, and data:

1. consumer application;
2. enterprise application with embedded generative AI;
3. organization-built application using a third-party pre-trained model;
4. third-party model fine-tuned with organization-specific data;
5. self-trained model.

The ownership model helps tailor evidence requests. Consumer and enterprise applications place more emphasis on provider terms, contractual protections, data use, and supplier resilience. Organization-built, fine-tuned, and self-trained models add direct responsibilities for architecture, threat modeling, data governance, model access, training/fine-tuning data, deployment, and monitoring.

AWS groups considerations across governance and compliance, legal and privacy, risk management, controls, and resilience.

## Selected source excerpts

> “The scopes are numbered 1–5, representing least ownership to greatest ownership.”

> “In the Generative AI Security Scoping Matrix, we identify five security disciplines that span the different types of generative AI solutions.”

> “Core security disciplines, like identity and access management, data protection, privacy and compliance, application security, and threat modeling are still critically important for generative AI workloads, just as they are for any other workload.”

## Use boundary

The scopes are a vendor mental model, not a regulatory classification. They can structure planning but cannot establish legal applicability, adequate control design, or operating effectiveness. ACME evidence must establish the actual service, ownership model, contracts, data handling, access paths, and resilience requirements. Consult both current official AWS sources before reliance.
