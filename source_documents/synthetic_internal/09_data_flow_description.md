# Data Flow Description: R&D AI Pilot

**Record owner:** R&D Digital Office, Data Engineering
**Approver:** R&D Data Council
**Status:** Version 0.8, controlled development
**Effective or as-of date:** 20 May 2026
**Review cycle:** At data-flow change

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

## Pending data-flow decision

The flow does not yet specify whether rejected documents are logged and whether rejection reasons reveal sensitive project metadata.

## Data-flow breakpoints

The main control breakpoints are intake approval, extraction quality check, retrieval relevance review, model-output review, use in a research record, supplier support access, and deletion/exit. The current flow description does not yet show how rejected outputs are retained for monitoring without becoming part of the scientific record.

## Data-flow narrative

A typical R&D AI interaction begins with a researcher selecting an approved workspace and asking a question against a bounded set of documents. The system retrieves relevant passages from source material, sends the prompt and selected context to an approved model endpoint, receives a draft answer, and stores the output with metadata. Where the user exports the answer into a project deck, study note, or decision packet, the output leaves the AI platform and becomes part of normal research records management.

The data flow is more complex for co-development projects. Supplier engineers may receive test data, anonymized examples, evaluation rubrics, defect reports, user feedback, and performance statistics. Each of these artifacts can reveal scientific priorities even if the original source documents are not transferred. The data-flow record therefore treats evaluation examples and feedback comments as controlled data.
