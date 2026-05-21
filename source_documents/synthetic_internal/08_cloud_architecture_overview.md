---
title: Cloud Architecture Overview for R&D AI Sandbox
doc_type: architecture
owner: Cloud Platform Team
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 08_cloud_architecture_overview.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: Cloud Architecture Overview for R&D AI Sandbox. scenario: AI in Research
  and Development planning evidence.'
Summary: 'title: Cloud Architecture Overview for R&D AI Sandbox. doc_type: architecture.
  owner: Cloud Platform Team. status: draft. company: ACME Pharma. confidentiality:
  Internal. scenario: AI in Research and Development planning evidence. Cloud Architecture
  Overview for R&D AI Sandbox. Environment summary. The proposed sandbox uses a segregated
  cloud account for AI experimentation.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Cloud Architecture Overview for R&D AI Sandbox


## Environment summary

The proposed sandbox uses a segregated cloud account for AI experimentation. The environment contains object storage for approved pilot documents, a managed vector index, an application layer for retrieval and summarization, and an approved model endpoint. Access is restricted to pilot users, the R&D AI product owner, and named support engineers.

## Control assumptions

- Separate development, test, and pilot environments.
- Identity federation with role-based access.
- Encryption at rest and in transit.
- Central logging for administrative actions and data access.
- No direct public access to storage or retrieval services.
- Network controls limiting egress to approved endpoints.
- Automated deletion process for pilot data after retention period.

## Open architecture questions

The current design does not yet show how prompt history, retrieved passages, model outputs, embeddings, or error traces are stored and classified. It also does not show whether vendor support personnel can access logs or payloads.

## Audit planning relevance

The cloud expert should assess technical design. Audit planning should focus on whether such specialist review occurred, whether high-risk assumptions are documented, and whether architecture evidence supports the claimed data restrictions.

## Architecture assumptions for audit planning

The ACME Pharma R&D AI sandbox uses a segregated project workspace, approved identity federation, restricted network paths, encrypted object storage, a retrieval index, model endpoint access, application logs, security logs, and a review queue for flagged outputs. The architecture diagram distinguishes source documents, text extracts, chunks, embeddings, prompts, retrieved passages, generated outputs, reviewer comments, and audit logs.

## Audit-relevant architecture questions

1. Are embeddings treated as derived confidential data and retained/deleted with the same rigor as source documents?
2. Are prompts and outputs logged in a way that supports traceability without over-retaining sensitive payloads?
3. Can administrators or supplier support staff view restricted R&D content, and is that access reviewed?
4. Are model endpoint calls restricted to approved regions and approved data classes?
5. Are sandbox-to-production promotion controls defined, or can teams clone the workspace informally?

## Architecture components

The R&D AI platform uses a private application layer, a managed retrieval store, approved model endpoints, and a workspace interface for researchers. Source documents are uploaded into controlled project workspaces. Text extraction and indexing occur inside the approved environment. Prompts combine user instructions, retrieved context, and system guidance. Outputs are stored with references to the source workspace, user, timestamp, and model version where technically available.

The architecture separates four storage areas: source files, extracted text, vector embeddings, and generated outputs. Security review requires each area to have a documented retention period, encryption setting, access model, and deletion path. Embeddings are treated as derived restricted data when generated from restricted source material, even though they are not human-readable. This treatment is conservative but avoids a common AI governance gap.

## Operational controls and gaps

Planned controls include single sign-on, role-based workspace access, environment separation for sandbox and routine use, logging of file upload and output export events, and quarterly access review for privileged roles. Model endpoint changes must be recorded because the same prompt and evidence set may produce different output after a model upgrade.

Current gaps include incomplete evidence of support access, unclear retention for failed prompts, and no automated reconciliation between the AI system inventory and cloud resources. The audit should request architecture diagrams, data-flow records, logging samples, model-change tickets, access-review evidence, and incident-response runbooks. The architecture should be tested against actual platform records rather than accepted as design intent.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 08 cloud architecture overview would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
