---
title: 'Incident Response Playbook: AI Data Leakage in R&D'
doc_type: playbook
owner: Security Incident Response
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 19_incident_response_playbook.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: ''Incident Response Playbook: AI Data Leakage in R&D''. scenario: AI
  in Research and Development planning evidence.'
Summary: 'title: ''Incident Response Playbook: AI Data Leakage in R&D''. doc_type:
  playbook. owner: Security Incident Response. status: draft. company: ACME Pharma.
  confidentiality: Internal. scenario: AI in Research and Development planning evidence.
  Incident Response Playbook: AI Data Leakage in R&D. Trigger examples. Vendor support
  accesses restricted material without approval.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Incident Response Playbook: AI Data Leakage in R&D


## Trigger examples

- Confidential research text is uploaded to an unapproved AI service.
- Vendor support accesses restricted material without approval.
- AI output exposes data from another project corpus.
- A prompt or log containing restricted research data is retained outside the approved environment.
- A third party cannot prove deletion of pilot data after engagement close.

## Response steps

1. Preserve evidence and identify affected data classes.
2. Disable access or stop processing where necessary.
3. Notify R&D owner, Security, Legal, Privacy, and TPRM.
4. Determine whether partner, regulator, or contractual notification is required.
5. Review external AI-provider retention and training terms.
6. Assess whether outputs, embeddings, logs, or caches must be deleted.
7. Document root cause and corrective action.

## Open question

The playbook does not yet define how to verify deletion from external AI-provider systems if data was incorporated into training or evaluation workflows.

## Incident scenarios

1. Restricted compound data uploaded to an unapproved AI endpoint.
2. Supplier support views a prompt containing unpublished target strategy.
3. AI output with fabricated citations is copied into a meeting pack.
4. A user exports model output and source snippets to an uncontrolled collaboration space.
5. A vendor subprocessor is discovered after pilot data has already been processed.
6. A retrieval or model change causes material degradation in negative-evidence detection.

## Response evidence

Each scenario requires event timeline, affected data class, users and support personnel involved, system/version context, source/output artifacts, containment action, deletion or return evidence, regulatory/Quality/Legal notification decision, and corrective action owner.

## Incident scenarios

The playbook defines AI-specific incident scenarios: restricted data entered into an unapproved tool, supplier access beyond the approved window, model output copied into a decision record without review, suspected leakage of partner-confidential material, unexpected model behavior after endpoint change, loss of source traceability, and inability to delete project data at exit. Each scenario has an intake route, initial containment step, required stakeholders, and evidence-preservation expectation.

The first containment step is usually to stop further use, preserve prompts and outputs where available, identify affected workspaces, and classify the data involved. Legal/IP, Privacy, Security, Quality, and the accountable R&D owner are involved depending on data class and decision impact. The playbook warns against deleting evidence before the impact assessment is complete.

## Open response questions

The playbook still needs clearer procedures for external model providers and co-development partners. It is not always clear whether ACME can require prompt/output preservation, supplier log export, or deletion confirmation within the required time. The playbook also does not yet define when a research-integrity review is needed after AI output influenced a decision packet.

The audit should test incident-readiness through tabletop evidence, not only the written playbook. A good sample scenario would involve restricted assay context pasted into an unapproved assistant and later copied into a project summary.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 19 incident response playbook would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.
