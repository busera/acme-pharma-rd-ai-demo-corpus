# Incident Response Playbook: AI Data Leakage in R&D

**Record owner:** Security Incident Response
**Approver:** R&D Digital Office and Legal/IP
**Status:** Version 1.0, approved
**Effective or as-of date:** 2 May 2026
**Review cycle:** Annual exercise

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

## Pending response decision

The playbook does not yet define how to verify deletion from external AI-provider systems if data was incorporated into training or evaluation workflows.

## Response evidence

Each scenario requires event timeline, affected data class, users and support personnel involved, system/version context, source/output artifacts, containment action, deletion or return evidence, regulatory/Quality/Legal notification decision, and corrective action owner.

## Incident scenarios

The playbook defines AI-specific incident scenarios: restricted data entered into an unapproved tool, supplier access beyond the approved window, model output copied into a decision record without review, suspected leakage of partner-confidential material, unexpected model behavior after endpoint change, loss of source traceability, and inability to delete project data at exit. Each scenario has an intake route, initial containment step, required stakeholders, and evidence-preservation expectation.

The first containment step is usually to stop further use, preserve prompts and outputs where available, identify affected workspaces, and classify the data involved. Legal/IP, Privacy, Security, Quality, and the accountable R&D owner are involved depending on data class and decision impact. The playbook warns against deleting evidence before the impact assessment is complete.

## Open response questions

The playbook still needs clearer procedures for external model providers and co-development partners. It is not always clear whether ACME can require prompt/output preservation, supplier log export, or deletion confirmation within the required time. The playbook also does not yet define when a research-integrity review is needed after AI output influenced a decision packet.
