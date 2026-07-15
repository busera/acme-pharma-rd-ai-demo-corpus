# Cloud Architecture Overview for R&D AI Sandbox

**Record owner:** R&D Digital Office, Platform Engineering
**Approver:** Security Architecture Review
**Status:** Version 0.8, controlled development
**Effective or as-of date:** 20 May 2026
**Review cycle:** At material architecture change

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


The ACME Pharma R&D AI sandbox uses a segregated project workspace, approved identity federation, restricted network paths, encrypted object storage, a retrieval index, model endpoint access, application logs, security logs, and a review queue for flagged outputs. The architecture diagram distinguishes source documents, text extracts, chunks, embeddings, prompts, retrieved passages, generated outputs, reviewer comments, and system logs.

## Architecture components

The R&D AI platform uses a private application layer, a managed retrieval store, approved model endpoints, and a workspace interface for researchers. Source documents are uploaded into controlled project workspaces. Text extraction and indexing occur inside the approved environment. Prompts combine user instructions, retrieved context, and system guidance. Outputs are stored with references to the source workspace, user, timestamp, and model version where technically available.

The architecture separates four storage areas: source files, extracted text, vector embeddings, and generated outputs. Security review requires each area to have a documented retention period, encryption setting, access model, and deletion path. Embeddings are treated as derived restricted data when generated from restricted source material, even though they are not human-readable. This treatment is conservative but avoids a common AI governance gap.

## Operational controls and gaps

Planned controls include single sign-on, role-based workspace access, environment separation for sandbox and routine use, logging of file upload and output export events, and quarterly access review for privileged roles. Model endpoint changes must be recorded because the same prompt and evidence set may produce different output after a model upgrade.
