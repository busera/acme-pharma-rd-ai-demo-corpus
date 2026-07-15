# Logging and Monitoring Summary

**Record owner:** R&D Digital Office, Platform Operations
**Approver:** Security
**Status:** Version 0.7, controlled development
**Effective or as-of date:** 16 June 2026
**Review cycle:** Monthly

## Logged events

The sandbox is expected to log authentication events, document ingestion events, permission changes, retrieval queries, model requests, administrative actions, export events, and deletion jobs.

## Monitoring objectives

- Detect unauthorized access to restricted project corpora.
- Identify unusually high query or export volume.
- Detect attempts to process restricted data classes.
- Monitor vendor support access.
- Support investigation of suspected leakage or incorrect output.

## Retention balance

Security wants sufficient retention for investigation. R&D and Legal are concerned that logs may contain sensitive prompts, retrieved passages, or research hypotheses. The retention design must balance traceability with data minimization.



## Monitoring signals

The monitoring plan tracks restricted-data upload attempts, blocked external-processing requests, high-impact prompts, output acceptance/rejection, reviewer overrides, retrieval with low source diversity, hallucinated or missing citations, supplier support access, configuration changes, export activity, and deletion failures.

## Tension in logging design

The team has not fully resolved the trade-off between traceability and data minimization. Payload logs help investigators reconstruct events, but they may also retain sensitive research content longer than the source document. The current proposal is to keep full payloads only in the approved evidence store, use hashed or redacted payload references in operational logs, and require elevated access for incident reconstruction.

## Events expected to be logged

The monitoring design expects logs for user login, workspace access, file upload, file deletion, prompt submission, retrieved-source reference, model endpoint used, output generation, output export, configuration change, supplier support access, failed policy checks, and incident reports. Logs should include user, timestamp, workspace, event type, and enough object reference to reconstruct what happened without exposing full restricted content in the log itself.

Monitoring is divided into operational monitoring and governance monitoring. Operational monitoring looks for errors, failed jobs, performance issues, model endpoint failures, and storage problems. Governance monitoring looks for unusual usage patterns, restricted data in the wrong workspace, output exports from high-risk workspaces, repeated use after pilot expiry, and supplier access outside approved windows.

## Current monitoring limitations

The summary notes that prompt and output content are not routinely inspected due to confidentiality concerns. Instead, monitoring relies on metadata, workspace classification, export events, and spot checks. This creates a residual risk that misuse may not be visible unless users self-report or a downstream record is reviewed.
