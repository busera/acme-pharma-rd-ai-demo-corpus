---
title: R&D AI Risk Register Extract
doc_type: risk register
owner: Enterprise Risk / R&D Risk Owner
status: working
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 13_risk_register_extract.md
IIA_Type: RCM
IIA_Type_Rational: The document is a risk register that maps identified risks to control
  maturity and residual concerns, aligning with the definition of a Risk and Control
  Matrix (RCM) used for audit planning.
Quality_Rating: M
Relevance_Score: H
Fact: The risk register identifies ten risk themes relevant to the audit objective,
  including confidential research data disclosure to external providers, vendor use
  of company material for training without approval, unclear ownership of co-developed
  artifacts, AI output influencing research direction without adequate expert review,
  retrieval missing critical negative results, cloud misconfiguration or excessive
  logging, lack of source traceability for model outputs, shadow AI bypassing inventory
  and approval, and exit process failures. The expanded register details specific
  risks such as RDAI-R01 (restricted R&D data processed outside approved boundary)
  with high inherent risk and unproven enforcement at upload, RDAI-R02 (supplier uses
  ACME content for training) with contract language under review and unclear derived
  artifacts, RDAI-R04 (AI output influences research direction without accountable
  scientist review) where evidence of review quality is limited, RDAI-R06 (GxP-relevant
  records created without Part 11 or data-integrity assessment) with unclear ownership
  of classification decisions, and RDAI-R08 (shadow AI use bypasses review) where
  training and policy are planned but unmet user demand exists. Several risks are
  not fully treated, with treatment depending on contract language, cloud review,
  data classification, pilot controls, and user training. The planning note cautions
  that the register is not the full risk universe and audit planning should challenge
  completeness, especially for IP, third-party, privacy, security, human review, and
  scientific integrity dimensions.
Summary: This internal working document is an extract from the R&D AI Risk Register.
  It presents ten risk themes covering data confidentiality, vendor misuse, intellectual
  property ownership, human review adequacy, retrieval completeness, cloud security,
  traceability, shadow IT, and exit procedures. The expanded risk register table lists
  specific risk IDs with inherent risk ratings, current control maturity, and residual
  concerns. For example, restricted data processing outside approved boundaries has
  high inherent risk but enforcement is unproven; supplier use of company content
  for training is under contract review but derived artifacts remain unclear; AI output
  influencing research direction lacks robust review evidence; GxP record creation
  without Part 11 assessment has unclear classification ownership; and shadow AI use
  persists despite planned training. The document notes that many risks are not fully
  treated and that mitigation relies on contract language, cloud review, data classification,
  pilot controls, and user training. A planning note emphasizes that the register
  should not be considered the complete risk universe and that audit planning must
  challenge completeness across IP, third-party, privacy, security, human review,
  and scientific integrity areas. The register serves as a starting point for identifying
  control gaps in the AI pilot governance, security, legal review, human control,
  and traceability domains.
Section_Context: Risk/control matrix
IIA_Relevance_Explanation: The document is a risk register that maps identified risks
  to control maturity and residual concerns, aligning with the definition of a Risk
  and Control Matrix (RCM) used for audit planning.
IIA_Relevance: H
IIA_Confidence: M
Notes: 'Auto-derived categorization: The document is a risk register that maps identified
  risks to control maturity and residual concerns, aligning with the definition of
  a Risk and Control Matr...'
---

# R&D AI Risk Register Extract


## Risk themes

1. Confidential research data disclosed to an external provider.
2. Vendor uses company material for training or product improvement without approval.
3. Co-developed artifacts have unclear ownership.
4. External personnel gain reusable confidential know-how.
5. AI output influences research direction without adequate expert review.
6. Retrieval misses critical negative results or contradictory evidence.
7. Cloud environment is misconfigured or logs sensitive payloads excessively.
8. Model outputs are copied into research records without source traceability.
9. Shadow AI use bypasses inventory and approval.
10. Exit process fails to delete or return research data and derived artifacts.

## Current treatment status

Several risks are identified but not fully treated. Treatment depends on contract language, cloud review, data classification, pilot controls, and user training.

## Planning note

The register is useful input, but it should not be treated as the full risk universe. Audit planning should challenge completeness, especially for IP, third-party, privacy, security, human review, and scientific integrity dimensions.

## Expanded risk register extract

| Risk ID | Risk theme | Inherent risk | Current control maturity | Residual concern |
|---|---|---|---|---|
| RDAI-R01 | Restricted R&D data processed outside approved boundary | High | Data-classification standard drafted | Enforcement at upload is not proven |
| RDAI-R02 | Supplier uses ACME content for training, support analytics, or product improvement | High | Contract language under review | Derived artifacts and telemetry remain unclear |
| RDAI-R03 | Co-developed prompts, embeddings, adapters, or evaluation sets have unclear ownership | Medium-high | SOW assigns some deliverables | Non-obvious work products not fully listed |
| RDAI-R04 | AI output influences research direction without accountable scientist review | High | Output review template exists | Evidence of review quality is limited |
| RDAI-R05 | Retrieval misses negative results or contradictory studies | Medium-high | Source-link requirement exists | Completeness checks are not mature |
| RDAI-R06 | GxP-relevant records are created without Part 11 or data-integrity assessment | High | GxP trigger questions drafted | Ownership of classification decision is unclear |
| RDAI-R07 | Cloud logs, prompts, or embeddings retain sensitive payloads longer than intended | High | Retention standard drafted | Technical deletion proof is pending |
| RDAI-R08 | Shadow AI use bypasses inventory, privacy, legal, and security review | Medium-high | Training and policy planned | Survey shows unmet user demand |
| RDAI-R09 | AI-generated regulatory language is reused beyond approved source evidence | High | Not approved for submission content | Future roadmap includes regulatory drafting |
| RDAI-R10 | External contributors keep access or know-how after project end | Medium-high | Offboarding checklist drafted | Supplier and collaborator evidence is fragmented |
| RDAI-R11 | Personal, coded subject, or collaborator data is processed without privacy basis | High | Privacy review in progress | Data-flow examples are incomplete |
| RDAI-R12 | Model changes degrade performance without detection | Medium-high | Change log exists | Regression-test library is immature |

## Planning note

The risk register is useful, but it is not complete enough to define audit scope by itself. Audit should challenge whether the highest-risk use cases are the ones with the best documentation, because informal or blocked use cases may produce more risk than the formal pilot.

## Governance and inventory risks added

| Risk ID | Risk theme | Inherent risk | Current control maturity | Residual concern |
|---|---|---|---|---|
| RDAI-R13 | AI use-case inventory and AI system inventory are not reconciled | Medium-high | Both inventories exist in draft | Shadow AI and unlinked systems may be missed |
| RDAI-R14 | Governance forum approval does not match actual system lifecycle state | Medium | Lifecycle gates drafted | Development teams may treat strategy approval as release approval |
| RDAI-R15 | External co-development project creates AI artifacts not covered by contract or inventory | High | Project NEURALIS charter drafted | Derived artifacts and know-how reuse remain unresolved |

## Risk-register interpretation notes

The risk register now separates root risks from observed issues. For example, incomplete metadata in the AI use-case register is not itself the main risk; it is evidence for a broader risk that AI governance cannot reliably identify high-risk use cases before expansion. Similarly, researcher use of public AI tools is an observed behavior that supports a shadow-AI risk, not a complete risk statement by itself.

The register groups risks into six themes: governance and inventory completeness, data quality and traceability, third-party co-development, privacy and confidentiality, GxP or submission-support boundary control, and scientific integrity. Each risk includes current control evidence, expected control evidence, and likely audit procedures. This structure is intended to support planning rather than final issue writing.

## Emerging risks from updated source pack

Newly added risks include inconsistency between the use-case inventory and system inventory, unclear ownership of co-developed prompts and evaluation sets, insufficient evidence that embeddings and feedback comments inherit source-data classification, and lack of monitoring for pilots that become routine through repeated use. Another important risk is model-change opacity: if an approved cloud model changes behavior without a documented impact assessment, prior evaluation evidence may no longer support current use.

The audit should prioritize risks where multiple documents point to the same weakness. Inventory gaps appear in the use-case register, system inventory, shadow-AI survey, and governance model. Third-party risks appear in the SOW, collaboration charter, legal questions, data flow, and offboarding standard. These cross-document patterns are stronger planning evidence than a single risk-register row.