---
title: Offboarding Checklist for External AI Contributors
doc_type: checklist
owner: R&D Partnerships / IAM
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 27_offboarding_external_contributors.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: Offboarding Checklist for External AI Contributors. scenario: AI in
  Research and Development planning evidence.'
Summary: 'title: Offboarding Checklist for External AI Contributors. doc_type: checklist.
  owner: R&D Partnerships / IAM. status: draft. company: ACME Pharma. confidentiality:
  Internal. scenario: AI in Research and Development planning evidence. Offboarding
  Checklist for External AI Contributors. Checklist. Confirm end date and remove system
  access.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Offboarding Checklist for External AI Contributors


## Checklist

- Confirm end date and remove system access.
- Retrieve or confirm deletion of local copies of company material.
- Confirm deletion of prompts, outputs, evaluation cases, embeddings, and support logs where applicable.
- Review whether any deliverables contain confidential research information.
- Confirm return of documentation, code, configuration, and co-developed artifacts owned by the company.
- Remind contributor of confidentiality, IP, and post-engagement obligations.
- Obtain written attestation when required by contract.

## Gap

The checklist is strong for access removal but weak on non-documentary know-how. Legal should define what can reasonably be controlled through confidentiality, conflict-of-interest, and non-use clauses.

## Offboarding sequence

External contributor offboarding requires account disablement, project-role removal, retrieval of ACME-owned work products, deletion or return of source data, confirmation for derived artifacts, review of open support tickets, confirmation of subprocessor obligations, final access-log review, and Legal/IP review of reusable know-how restrictions.

## Evidence gap

The checklist handles named user accounts well but is less mature for service accounts, shared workspaces, vendor-managed notebooks, exported evaluation sets, and embeddings. Audit should test offboarding with one real project closeout rather than relying only on the checklist.

## Offboarding triggers

Offboarding is required when a supplier engagement ends, a subcontractor leaves the project, a co-development phase closes, a support role is no longer needed, or a project workspace is retired. The process applies to named supplier users, shared technical accounts, development environments, collaboration folders, test data, support logs, evaluation examples, and retained artifacts.

The process owner must confirm access revocation, return or deletion of data, closure of support channels, transfer of deliverables, final defect list, and retained-artifact statement. For co-development projects, the retained-artifact statement is especially important because prompts, evaluation rubrics, workflow designs, and reviewer feedback may represent ACME-derived know-how.

## Evidence expectations

Required evidence includes access-removal screenshots or reports, supplier attestation, subprocessor confirmation if applicable, deletion logs, final deliverable inventory, unresolved-risk list, and business-owner acceptance. Legal/IP must review any supplier request to retain generic components developed during the project.

The audit should test whether offboarding happens when pilot phases end, not only when contracts terminate. A supplier may retain access after a "temporary" pilot if no one owns offboarding for research collaborations.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 27 offboarding external contributors would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.

## Example offboarding packet

For a completed co-development pilot, the offboarding packet should include a named supplier-user list, workspace list, data-package list, retained-artifact register, deletion certificate, and ACME business-owner acceptance. The retained-artifact register should separate generic supplier components from ACME-derived materials such as prompt templates, evaluation examples, reviewer comments, defect labels, and scientific decision criteria. Any retained ACME-derived material requires Legal/IP approval and a documented business rationale.

The packet should also confirm whether backups, telemetry, support tickets, and subprocessors are covered by deletion or retention commitments. This is important because visible workspace deletion may not remove derived records from operational support systems.
