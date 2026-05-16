---
title: Logging and Monitoring Summary
doc_type: monitoring summary
owner: Security Operations
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 18_logging_monitoring_summary.md
IIA_Type: GOV
IIA_Type_Rational: This document outlines the logging and monitoring design for the
  AI sandbox, which is a key governance control for traceability and security. It
  describes monitoring objectives, logged events, and design tensions, making it a
  governance document.
Quality_Rating: M
Relevance_Score: H
Fact: The sandbox logging design expects to capture authentication, document ingestion,
  permission changes, retrieval queries, model requests, administrative actions, exports,
  and deletions. Monitoring objectives include detecting unauthorized access to restricted
  project corpora, unusually high query or export volume, attempts to process restricted
  data classes, and vendor support access. There is an unresolved tension between
  auditability and data minimization because logs may contain sensitive prompts, retrieved
  passages, or research hypotheses. The current proposal is to keep full payloads
  only in an approved evidence store, use hashed or redacted payload references in
  operational logs, and require elevated access for incident reconstruction. Monitoring
  is split into operational monitoring (errors, performance, model endpoint failures)
  and governance monitoring (unusual usage patterns, restricted data in wrong workspace,
  exports from high-risk workspaces, repeated use after pilot expiry, supplier access
  outside approved windows). The summary acknowledges current monitoring limitations.
Summary: The document is a draft logging and monitoring summary for the AI sandbox.
  It lists the types of events expected to be logged, including authentication, document
  ingestion, permission changes, retrieval queries, model requests, administrative
  actions, exports, and deletions. The monitoring objectives focus on detecting unauthorized
  access, unusual query or export volumes, attempts to process restricted data, vendor
  support access, and supporting investigations. A key tension is balancing auditability
  with data minimization, as logs may contain sensitive research content. The proposed
  solution is to store full payloads only in an approved evidence store, use hashed
  or redacted references in operational logs, and require elevated access for incident
  reconstruction. Monitoring is divided into operational monitoring for errors and
  performance, and governance monitoring for unusual usage patterns and policy violations.
  The document also notes that the team has not fully resolved the trade-off between
  auditability and data minimization, and that current monitoring limitations exist.
Section_Context: Governance framework
IIA_Relevance_Explanation: This document outlines the logging and monitoring design
  for the AI sandbox, which is a key governance control for traceability and security.
  It describes monitoring objectives, logged events, and design tensions, mak...
IIA_Relevance: H
IIA_Confidence: M
Notes: 'Auto-derived categorization: This document outlines the logging and monitoring
  design for the AI sandbox, which is a key governance control for traceability and
  security. It describes mo...'
---

# Logging and Monitoring Summary


## Logged events

The sandbox is expected to log authentication events, document ingestion events, permission changes, retrieval queries, model requests, administrative actions, export events, and deletion jobs.

## Monitoring objectives

- Detect unauthorized access to restricted project corpora.
- Identify unusually high query or export volume.
- Detect attempts to process restricted data classes.
- Monitor vendor support access.
- Support investigation of suspected leakage or incorrect output.

## Retention balance

Security wants sufficient retention for investigation. R&D and Legal are concerned that logs may contain sensitive prompts, retrieved passages, or research hypotheses. The retention design must balance auditability with data minimization.

## Planning implication

Audit planning should ask what exactly is logged, who can read logs, whether payloads are redacted, and how retention aligns with legal and research confidentiality needs.

## Monitoring signals

The monitoring plan tracks restricted-data upload attempts, blocked external-processing requests, high-impact prompts, output acceptance/rejection, reviewer overrides, retrieval with low source diversity, hallucinated or missing citations, supplier support access, configuration changes, export activity, and deletion failures.

## Tension in logging design

The team has not fully resolved the trade-off between auditability and data minimization. Payload logs help investigators reconstruct events, but they may also retain sensitive research content longer than the source document. The current proposal is to keep full payloads only in the approved evidence store, use hashed or redacted payload references in operational logs, and require elevated access for incident reconstruction.

## Events expected to be logged

The monitoring design expects logs for user login, workspace access, file upload, file deletion, prompt submission, retrieved-source reference, model endpoint used, output generation, output export, configuration change, supplier support access, failed policy checks, and incident reports. Logs should include user, timestamp, workspace, event type, and enough object reference to reconstruct what happened without exposing full restricted content in the log itself.

Monitoring is divided into operational monitoring and governance monitoring. Operational monitoring looks for errors, failed jobs, performance issues, model endpoint failures, and storage problems. Governance monitoring looks for unusual usage patterns, restricted data in the wrong workspace, output exports from high-risk workspaces, repeated use after pilot expiry, and supplier access outside approved windows.

## Current monitoring limitations

The summary notes that prompt and output content are not routinely inspected due to confidentiality concerns. Instead, monitoring relies on metadata, workspace classification, export events, and spot checks. This creates a residual risk that misuse may not be visible unless users self-report or a downstream record is reviewed.

The audit should request sample logs, monitoring dashboards, alert definitions, review evidence, and examples of follow-up actions. It should also test whether monitoring covers co-development environments, not only the production user workspace.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 18 logging monitoring summary would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.