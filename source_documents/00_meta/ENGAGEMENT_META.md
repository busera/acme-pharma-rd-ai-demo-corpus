---
audit_id: DEMO-RND-AI-001
audit_name: ACME Pharma AI in Research and Development Planning Review
audit_objective: Assess whether ACME Pharma R&D AI pilots are governed, secure, legally
  reviewed, human-controlled, and traceable before expansion beyond a sandbox.
audit_context: ACME Pharma R&D AI audit-planning scenario. Central source-status disclosure
  is maintained in DEMO_SOURCE_STATEMENT.md.
Document_File_Name: ENGAGEMENT_META.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'audit_name: ACME Pharma AI in Research and Development Planning Review. audit_objective:
  Assess whether ACME Pharma R&D AI pilots are governed, secure, legally.'
Summary: 'audit_id: DEMO-RND-AI-001. audit_name: ACME Pharma AI in Research and Development
  Planning Review. audit_objective: Assess whether ACME Pharma R&D AI pilots are governed,
  secure, legally. reviewed, human-controlled, and traceable before expansion beyond
  a sandbox. audit_context: ACME Pharma R&D AI audit-planning scenario. Central source-status
  disclosure. is maintained in DEMO_SOURCE_STATEMENT.md. Risk Planning Taxonomy. Initial
  Team Risk Hypotheses.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
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

ACME Pharma is modeled as a 50,000-employee global life-sciences company with about 9,000 R&D employees. The audit planning focus is the R&D AI portfolio, including literature intelligence, experiment-design challenge, lab-note synthesis, candidate prioritization, patent landscape support, and future regulatory drafting support.

The audit should treat AI in R&D as a cross-functional risk topic. The planning basis needs R&D leadership, R&D Digital Office, Quality, Regulatory Science, Legal/IP, Privacy, Security, Procurement, Third Party Risk Management, Data Stewardship, supplier management, and research-user evidence.
