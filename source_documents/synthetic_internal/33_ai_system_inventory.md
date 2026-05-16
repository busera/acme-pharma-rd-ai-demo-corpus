---
title: ACME Pharma R&D AI system inventory extract
company: ACME Pharma
doc_type: system inventory extract
owner: Enterprise Architecture / AI Governance Office
status: working
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 33_ai_system_inventory.md
IIA_Type: EVD
IIA_Type_Rational: This document is an AI system inventory extract that provides factual
  evidence of the current AI systems in R&D, their lifecycle states, and identified
  control gaps, directly supporting the audit objective to assess governance and traceability.
Quality_Rating: H
Relevance_Score: H
Fact: 'The inventory records nine AI systems used or planned in R&D, maintained by
  Enterprise Architecture with input from AI Governance, R&D Digital Office, Security,
  Data Stewardship, and system owners. Systems are in various lifecycle states: Running,
  Running pilot, In development, On hold, and Proposed. Several systems have significant
  control gaps: SYS-AI-001 has limited source-quality monitoring; SYS-AI-002 lacks
  consistent evidence of support access reviews; SYS-AI-003 has pending derived artifact
  ownership and GxP classification; SYS-AI-004 shows weak portfolio decision traceability;
  SYS-AI-005 has unresolved Part 11, data integrity, and validation approach; SYS-AI-006
  has unresolved privilege, IP reuse, and supplier training terms; SYS-AI-007 has
  an undefined submission-support boundary and quality review model; SYS-AI-008 has
  thin vendor change notification and evaluation evidence. The inventory also notes
  that SYS-AI-009, External General AI Tools, is listed but the snippet is incomplete.
  These gaps directly relate to governance, security, legal review, human control,
  and traceability concerns for AI pilots before expansion.'
Summary: The document is an extract from the ACME Pharma R&D AI system inventory,
  which records technical AI solutions used or planned in R&D. It is maintained by
  Enterprise Architecture with cross-functional input and must reconcile with business
  use cases, supplier records, cloud assets, model lifecycle documentation, and retirement
  plans. The extract presents a table of nine AI systems, each with a system ID, AI
  system name, type, hosting/supplier model, lifecycle state, supported use cases,
  highest data class, monitoring status, and key control gap. The systems range from
  a knowledge search assistant and an insight workspace to a co-developed experiment-design
  assistant, a candidate evidence ranker, a lab record drafting assistant, a patent
  landscape copilot, a regulatory drafting support tool, a partner intelligence feed,
  and external general AI tools. Lifecycle states include Running, Running pilot,
  In development, On hold, and Proposed, indicating a mix of operational and pre-operational
  systems. Monitoring statuses vary from basic usage and citation monitoring to blocked-request
  and reviewer-disposition monitoring, test monitoring only, reviewer override tracking,
  and none. Key control gaps highlight deficiencies in source-quality monitoring,
  support access review evidence, derived artifact ownership and GxP classification,
  portfolio decision traceability, Part 11 and data integrity compliance, privilege
  and IP reuse terms, submission-support boundary definition, and vendor change notification
  evaluation. The inventory serves as a foundational record for assessing the governance,
  security, legal, human-control, and traceability posture of AI pilots before any
  expansion beyond the sandbox.
Section_Context: Evidence artifact
IIA_Relevance_Explanation: This document is an AI system inventory extract that provides
  factual evidence of the current AI systems in R&D, their lifecycle states, and identified
  control gaps, directly supporting the audit objective to assess g...
IIA_Relevance: H
IIA_Confidence: H
Notes: 'Auto-derived categorization: This document is an AI system inventory extract
  that provides factual evidence of the current AI systems in R&D, their lifecycle
  states, and identified contr...'
---

# ACME Pharma R&D AI system inventory extract

## Inventory purpose

The AI system inventory records the technical AI solutions used or planned in R&D. It is maintained by Enterprise Architecture with input from AI Governance, R&D Digital Office, Security, Data Stewardship, and system owners. The inventory must reconcile to business use cases, supplier records, cloud assets, model lifecycle documentation, and retirement plans.

## System inventory extract

| System ID | AI system | Type | Hosting / supplier model | Lifecycle state | Supported use cases | Highest data class | Monitoring status | Key control gap |
|---|---|---|---|---|---|---|---|---|
| SYS-AI-001 | Knowledge Search Assistant | RAG / semantic search | ACME-managed workspace with approved external model endpoint | Running | UC-RD-001 | Public | Basic usage and citation monitoring | Source-quality monitoring limited |
| SYS-AI-002 | R&D Insight Workspace | Summarization and source comparison | ACME cloud tenant with vendor support | Running pilot | UC-RD-002 | Restricted internal | Blocked-request and reviewer-disposition monitoring | Support access review not consistently evidenced |
| SYS-AI-003 | Project NEURALIS Assistant | Co-developed RAG and experiment-design challenge workflow | ACME tenant, HelixBridge co-development support | In development | UC-RD-003 | Restricted internal | Test monitoring only | Derived artifact ownership and GxP classification pending |
| SYS-AI-004 | Candidate Evidence Ranker | Ranking / decision-support workflow | ACME-built model pipeline with external components | Running pilot | UC-RD-004 | Restricted research | Reviewer override tracked | Portfolio decision traceability weak |
| SYS-AI-005 | Lab Record Drafting Assistant | Draft generation from lab records | Proposed vendor-hosted workflow | On hold | UC-RD-005 | GxP / study record data | None | Part 11, data integrity, and validation approach unresolved |
| SYS-AI-006 | Patent Landscape Copilot | Search, summarization, comparison | External SaaS with ACME restricted tenant | In development | UC-RD-006 | Confidential invention notes | Not operational | Privilege, IP reuse, and supplier training terms unresolved |
| SYS-AI-007 | Regulatory Drafting Support | Controlled-source drafting assistant | Not selected | Proposed | UC-RD-007 | Approved regulatory source docs | None | Submission-support boundary and quality review model undefined |
| SYS-AI-008 | Partner Intelligence Feed | Monitoring and summarization feed | Supplier-managed public-data feed | Running | UC-RD-009 | Public plus partner watchlist | Supplier service reports only | Vendor change notification and evaluation evidence thin |
| SYS-AI-009 | External General AI Tools | Unapproved public AI tools | External public tools | Running unofficially | UC-RD-010 | Unknown | No formal monitoring | Shadow AI and data leakage risk |

## System lifecycle fields expected but incomplete

- Model or service version.
- Intended-use statement linked to each use case.
- Data-flow diagram and highest data class.
- Supplier and subprocessor list.
- Model card or equivalent system description.
- Evaluation and acceptance evidence.
- Change-control owner and release history.
- Monitoring plan and incident categories.
- Retirement and deletion procedure.

## Reconciliation risks

1. A business use case can be registered without the supporting AI system being fully documented.
2. A system can exist in cloud or procurement records before AI Governance has classified it.
3. Vendor-hosted tools can be treated as ordinary SaaS even when prompts, outputs, embeddings, or reviewer feedback create AI-specific artifacts.
4. A system can move from public data to restricted data without a new intended-use or data-classification decision.
5. Shadow AI may never appear in the system inventory unless procurement, network, browser, expense, survey, and user-interview evidence is reconciled.

## System inventory fields

The system inventory records platform name, system owner, business owner, lifecycle state, model endpoint, hosting pattern, data stores, access model, supplier role, highest approved data class, GxP boundary, monitoring owner, and linked use cases. It also records whether the system stores source documents, extracted text, embeddings, prompts, outputs, feedback, telemetry, and audit logs.

The inventory distinguishes approved systems from systems in development and external tools reported through survey or procurement review. A system can be approved for one data class and prohibited for another. Approval is therefore tied to intended use and data boundary, not only to the tool name.

## Control use

Governance uses the system inventory to trigger access reviews, model-change assessments, supplier reviews, retention checks, and incident response coverage. The inventory should reconcile to cloud resources, identity groups, procurement records, and use-case records. If a cloud workspace exists but no system record exists, the governance inventory is incomplete. If a system record exists but no current use case is linked, the system may be orphaned or awaiting retirement.

The audit should request the latest system inventory extract and test three links: system to use case, system to access records, and system to supplier contract. These links show whether the inventory is operational or merely descriptive.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 33 ai system inventory would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.