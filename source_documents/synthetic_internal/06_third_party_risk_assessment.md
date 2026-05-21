---
title: Third Party Risk Assessment Summary
doc_type: assessment
owner: Third Party Risk Management
status: in review
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 06_third_party_risk_assessment.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: Third Party Risk Assessment Summary. scenario: AI in Research and Development
  planning evidence.'
Summary: 'title: Third Party Risk Assessment Summary. doc_type: assessment. owner:
  Third Party Risk Management. status: in review. company: ACME Pharma. confidentiality:
  Internal. scenario: AI in Research and Development planning evidence. Third Party
  Risk Assessment Summary. Assessment scope. The assessment covers the proposed R&D
  AI implementation partner and a cloud-hosted model service.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Third Party Risk Assessment Summary


## Assessment scope

The assessment covers the proposed R&D AI implementation partner and a cloud-hosted model service. The planned pilot would process public literature, internal research summaries, experiment protocols, and selected lab-note excerpts after redaction.

## Preliminary risk view

- Data confidentiality risk: high if unpublished research content is sent to external services without no-training and retention restrictions.
- Operational dependency risk: medium because the pilot is not yet production-critical, but future adoption could create vendor lock-in.
- Subcontractor risk: unknown because the implementation partner has not provided a full subcontractor list.
- Data residency risk: open pending cloud architecture confirmation.
- Exit risk: medium because deletion evidence and export format are not yet defined.

## Evidence requested

1. Security whitepaper and assurance reports.
2. Data processing agreement.
3. Model training and retention terms.
4. Subprocessor list.
5. Architecture and data-flow diagram.
6. Access control model for vendor staff.
7. Evidence of secure deletion after pilot.

## Planning implication

The audit should not treat vendor approval as complete until Legal, Privacy, Security, and business risk ownership have each documented their review.

## Third-party risk view

The current third-party assessment rates the supplier as high inherent risk because it processes restricted R&D information, operates a cloud-hosted AI workflow, supports configuration changes, and can access support logs. Residual risk is not yet supported because three key controls are still pending: contractual restriction on all forms of training/product improvement, independent review of the cloud data-flow diagram, and operational evidence that support access is logged and reviewed.

## Open TPRM findings

1. The supplier questionnaire answers are strong on enterprise security certifications but weak on R&D-specific data segregation.
2. The privacy review covers employee users but not all collaborator and coded subject-data edge cases.
3. The exit plan describes source-file deletion but does not explain embeddings, cached prompts, monitoring logs, or evaluation datasets.
4. The SOW permits supplier improvement recommendations, but the boundary between configuration advice and reusable product learning is not clear.

## Risk-assessment scope

The third-party assessment covers the supplier's hosting environment, model access pattern, support operations, subprocessors, incident response obligations, and data-use restrictions. The assessment is scoped to R&D AI support, not general corporate IT. This distinction matters because R&D prompts may include unpublished hypotheses, target-selection rationale, assay anomalies, partner-confidential context, and early scientific judgments that do not look like personal data but may still be highly sensitive.

The assessment identified four dependency types. Infrastructure dependency concerns where prompts, files, embeddings, and outputs are stored. Model dependency concerns which model endpoint processes the content and whether model updates can change output behavior. People dependency concerns supplier support and engineering access. Contract dependency concerns rights to reuse artifacts, telemetry, feedback, and learned implementation patterns.

## Residual assessment notes

The current residual risk is rated medium-high until three items are closed. First, the supplier must provide clearer evidence that ACME prompts and outputs are not used for training, fine-tuning, benchmarking, or product improvement. Second, the support-access process must show how emergency access is approved, logged, reviewed, and revoked. Third, the subprocessor list must explicitly address any service that could receive prompts, files, embeddings, output text, telemetry, or backups.

The assessment also flags concentration risk. If multiple R&D use cases adopt the same supplier platform, a weakness in data segregation, logging, or model-change management could affect literature review, experiment design, candidate prioritization, and regulatory drafting support at once. The audit should test whether vendor risk is assessed per use case only, or at the platform level as well.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 06 third party risk assessment would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
