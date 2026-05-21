---
title: 'Data Flow Description: R&D AI Pilot'
doc_type: data flow
owner: R&D Digital Office
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 09_data_flow_description.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: ''Data Flow Description: R&D AI Pilot''. scenario: AI in Research and
  Development planning evidence.'
Summary: 'title: ''Data Flow Description: R&D AI Pilot''. doc_type: data flow. owner:
  R&D Digital Office. status: draft. company: ACME Pharma. confidentiality: Internal.
  scenario: AI in Research and Development planning evidence. Data Flow Description:
  R&D AI Pilot. Flow summary. Approved source documents are collected from R&D project
  owners.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Data Flow Description: R&D AI Pilot


## Flow summary

1. Approved source documents are collected from R&D project owners.
2. Documents are screened for data class and third-party restrictions.
3. Permitted documents are loaded into a controlled repository.
4. Text is extracted or normalized into machine-readable form.
5. The system creates search indexes and retrieval-ready chunks.
6. A researcher asks a question or requests a planning challenge.
7. The workflow retrieves relevant passages and broader document context.
8. The model drafts a response with source references and uncertainty notes.
9. The researcher reviews the response, corrects assumptions, and records whether the output influenced a decision.

## Control points

Data classification occurs before ingestion. Retrieval should not cross project boundaries. Output review remains a human responsibility. Logs must be retained long enough to support incident review, but not so long that sensitive research traces are retained unnecessarily.

## Unresolved issue

The flow does not yet specify whether rejected documents are logged and whether rejection reasons reveal sensitive project metadata.

## Data-flow narrative

A researcher uploads approved source material to the R&D AI workspace. The system records source owner, data class, intended use, project code, source version, extraction status, and deletion date. Text is normalized for search and review, split into retrievable passages, and indexed. User prompts retrieve relevant passages and generate a draft answer. The draft answer is stored with source references, reviewer comments, and disposition: accepted, edited, rejected, or escalated.

## Data-flow breakpoints

The main control breakpoints are intake approval, extraction quality check, retrieval relevance review, model-output review, use in a research record, supplier support access, and deletion/exit. The current flow description does not yet show how rejected outputs are retained for monitoring without becoming part of the scientific record.

## Data-flow narrative

A typical R&D AI interaction begins with a researcher selecting an approved workspace and asking a question against a bounded set of documents. The system retrieves relevant passages from source material, sends the prompt and selected context to an approved model endpoint, receives a draft answer, and stores the output with metadata. Where the user exports the answer into a project deck, study note, or decision packet, the output leaves the AI platform and becomes part of normal research records management.

The data flow is more complex for co-development projects. Supplier engineers may receive test data, anonymized examples, evaluation rubrics, defect reports, user feedback, and performance statistics. Each of these artifacts can reveal scientific priorities even if the original source documents are not transferred. The data-flow record therefore treats evaluation examples and feedback comments as controlled data.

## Audit-relevant transfer points

The highest-risk transfer points are file upload, text extraction, embedding creation, prompt assembly, model processing, output storage, export, support access, telemetry, and deletion. The process owner must show what data class is allowed at each point, who can access it, how long it is retained, whether it can be reused, and how deletion is evidenced.

The audit should test one running use case and one development use case end to end. It should compare the documented data flow to actual configuration, logs, user guidance, and supplier commitments. Differences often appear around telemetry, support access, and exported outputs rather than the main user interface.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 09 data flow description would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
