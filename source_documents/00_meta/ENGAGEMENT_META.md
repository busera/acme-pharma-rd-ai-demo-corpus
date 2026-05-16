---
audit_id: DEMO-RND-AI-001
audit_name: ACME Pharma AI in Research and Development Planning Review
audit_objective: Assess whether ACME Pharma R&D AI pilots are governed, secure, legally
  reviewed, human-controlled, and traceable before expansion beyond a sandbox.
audit_context: ACME Pharma R&D AI audit-planning scenario. Central source-status disclosure
  is maintained in DEMO_SOURCE_STATEMENT.md.
Document_File_Name: ENGAGEMENT_META.md
IIA_Type: WP
IIA_Type_Rational: This document is an internal audit planning work paper that records
  risk taxonomy and initial risk hypotheses for the engagement, serving as a foundational
  planning document.
Quality_Rating: H
Relevance_Score: H
Fact: 'The document identifies eight risk areas relevant to the audit objective: R&D
  data governance (confidential data processed by external AI), third-party/co-development
  (unclear vendor rights to model artifacts), cloud/security (sandbox architecture
  exposing prompts and logs), scientific integrity (AI output influencing research
  without expert review), lifecycle and validation (pilot expansion before maturity),
  GxP and electronic records (AI output copied into controlled records), privacy and
  personal data (researcher or clinical-adjacent data entering AI workflows), and
  data quality and retrieval (AI missing negative results or outdated sources). Initial
  team risk hypotheses include confidential research material sent to external AI
  services before legal, privacy, security, and TPRM reviews are complete; vendor
  contracts not clearly restricting model training, product improvement, or reuse
  of know-how; unclear ownership of co-developed artifacts like prompts, embeddings,
  and evaluation cases; cloud architecture not fully showing where prompts, retrieved
  passages, outputs, embeddings, logs, and caches are stored; AI-generated summaries
  or experiment suggestions influencing scientific decisions without sufficient source
  review and accountable sign-off; and shadow AI use because researchers need faster
  literature and protocol support than approved tools provide. The ACME Pharma context
  describes an 80,000-employee global life-sciences company with about 14,500 R&D
  employees, focusing the audit on the R&D AI portfolio including literature intelligence,
  experiment-design challenge, lab-note synthesis, and candidate screening.'
Summary: "The document serves as an engagement meta file for the ACME Pharma AI in\
  \ Research and Development Planning Review. It presents a risk planning taxonomy\
  \ table that maps eight key areas\u2014R&D data governance, third-party/co-development,\
  \ cloud/security, scientific integrity, lifecycle and validation, GxP and electronic\
  \ records, privacy and personal data, and data quality and retrieval\u2014to example\
  \ risk themes and their planning relevance for the audit. Following the table, the\
  \ document lists six initial team risk hypotheses that elaborate on potential issues\
  \ such as premature exposure of confidential research material to external AI services,\
  \ inadequate vendor contract restrictions on model training and know-how reuse,\
  \ ambiguous ownership of co-developed AI artifacts, incomplete cloud architecture\
  \ transparency, insufficient human review of AI-generated scientific suggestions,\
  \ and the presence of shadow AI due to unmet researcher needs. The final section\
  \ provides ACME Pharma context, noting the company's scale (80,000 employees, 14,500\
  \ in R&D) and the audit's focus on the R&D AI portfolio, which includes applications\
  \ like literature intelligence, experiment design, lab-note synthesis, and candidate\
  \ screening. The content directly supports the audit objective by framing the governance,\
  \ security, legal, human-control, and traceability risks associated with AI pilots\
  \ before expansion beyond a sandbox."
Section_Context: Workpaper summary
IIA_Relevance_Explanation: This document is an internal audit planning work paper
  that records risk taxonomy and initial risk hypotheses for the engagement, serving
  as a foundational planning document.
IIA_Relevance: H
IIA_Confidence: H
Notes: 'Auto-derived categorization: This document is an internal audit planning work
  paper that records risk taxonomy and initial risk hypotheses for the engagement,
  serving as a foundational p...'
---

# Risk Planning Taxonomy

| Area | Example Risk Theme | Planning Relevance |
|---|---|---|
| R&D data governance | Confidential research data processed by external AI services | Helps define data classification and no-training evidence requests |
| Third-party / co-development | Unclear vendor rights to use model artifacts, prompts, embeddings, and project know-how | Helps define Legal, IP, and TPRM dependencies |
| Cloud/security | Sandbox architecture may expose prompts, outputs, logs, or embeddings | Helps define specialist cloud/security review needs |
| Scientific integrity | AI output may influence research direction without adequate expert review | Helps define human-in-the-loop controls |
| Lifecycle and validation | Pilot may expand before intended use, acceptance criteria, monitoring, and change control are mature | Helps define governance and readiness checks |
| GxP and electronic records | AI output may be copied into controlled records or used for submission-support decisions | Helps define Part 11, data integrity, and validation/assurance evidence needs |
| Privacy and personal data | Researcher, collaborator, coded subject, or clinical-adjacent data may enter AI workflows | Helps define privacy impact, minimization, and lawful-basis review |
| Data quality and retrieval | AI may miss negative results, outdated sources, or contradictory evidence | Helps define source-quality and reviewer-challenge procedures |


# Initial Team Risk Hypotheses

- Confidential research material may be sent to external AI services before Legal, Privacy, Security, and TPRM reviews are complete.
- Vendor contracts may not clearly restrict model training, product improvement, support access, subcontracting, retention, and reuse of know-how.
- Co-developed artifacts such as prompts, embeddings, evaluation cases, model adapters, and workflow documentation may have unclear ownership.
- Cloud architecture may not fully show where prompts, retrieved passages, outputs, embeddings, logs, and caches are stored.
- AI-generated summaries or experiment suggestions may influence scientific decisions without sufficient source review and accountable sign-off.
- Shadow AI use may exist because researchers need faster literature and protocol support than approved tools currently provide.

# ACME Pharma context for planning

ACME Pharma is modeled as an 80,000-employee global life-sciences company with about 14,500 R&D employees. The audit planning focus is the R&D AI portfolio, including literature intelligence, experiment-design challenge, lab-note synthesis, candidate prioritization, patent landscape support, and future regulatory drafting support.

The audit should treat AI in R&D as a cross-functional risk topic. The planning basis needs R&D leadership, R&D Digital Office, Quality, Regulatory Science, Legal/IP, Privacy, Security, Procurement, Third Party Risk Management, Data Stewardship, supplier management, and research-user evidence.