---
title: Access Control Matrix for R&D AI Sandbox
doc_type: access control
owner: Identity and Access Management
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 17_access_control_matrix.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: 'title: Access Control Matrix for R&D AI Sandbox. scenario: AI in Research and
  Development planning evidence.'
Summary: 'title: Access Control Matrix for R&D AI Sandbox. doc_type: access control.
  owner: Identity and Access Management. status: draft. company: ACME Pharma. confidentiality:
  Internal. scenario: AI in Research and Development planning evidence. Access Control
  Matrix for R&D AI Sandbox. Roles. Control expectations.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

# Access Control Matrix for R&D AI Sandbox


## Roles

| Role | Main permissions | Review requirement |
|---|---|---|
| Pilot Researcher | Ask questions against approved project corpus | manager approval |
| Principal Scientist | Approve experiment-design use | R&D leadership approval |
| R&D AI Product Owner | Manage use-case record and user access | quarterly access review |
| Support Engineer | Troubleshoot application layer | break-glass or ticketed access |
| Vendor Specialist | Limited configuration support | Legal/TPRM approval and time-bound account |
| Auditor / Reviewer | Read-only evidence access | engagement approval |

## Control expectations

Access should be least privilege, time-bound for external personnel, logged, and reviewed periodically. Shared accounts are not permitted. Vendor support must not access research content unless explicitly approved.

## Gap

The current matrix does not define who can export retrieved passages, prompt history, embeddings, or generated outputs.

## Role-based access model

| Role | Access | Restriction |
|---|---|---|
| Research user | Approved projects and approved data classes | No admin access, no export of restricted logs |
| Scientific reviewer | Review queue, source references, disposition fields | Cannot change system configuration |
| Data steward | Data-class approvals, retention metadata | Cannot approve scientific use |
| Product owner | Use-case settings, release notes | Cannot override GxP classification alone |
| Supplier support | Break-glass support only | Time-bound, ticket-bound, logged, reviewed |
| Security operations | Security logs and alerts | Payload access minimized |
| Quality/Regulatory reviewer | GxP assessment package and controlled evidence | Read-only unless assigned approver role |

## Access weaknesses

Current evidence shows strong identity federation but weaker evidence around supplier break-glass access, dormant collaborators, and whether privileged users can view restricted prompts or outputs outside the application review workflow.

## Role model

The access model defines separate roles for viewer, researcher, project owner, data steward, system administrator, supplier support, and governance reviewer. Researchers can query approved workspaces but cannot change retention settings, supplier configuration, or model endpoints. Project owners can approve workspace membership and export outputs. Data stewards approve data-classification decisions and source-corpus changes. System administrators manage platform configuration but should not routinely access research content.

Supplier support access is treated as privileged and time-bound. The matrix requires named approval, reason for access, scope, start and end time, logging, and post-access review. Emergency access must be reviewed after the fact. Shared support accounts are not permitted.

## Audit test considerations

The matrix should be compared against actual identity and platform records. The audit should test whether leavers were removed, whether supplier access expired, whether privileged roles are reviewed, and whether project owners understand their approval responsibility. It should also verify that access to embeddings, logs, exports, and support diagnostics is covered, not only access to the visible user interface.

A likely weakness is inherited access from broad R&D groups. If a workspace contains restricted project material, membership should be based on project need, not general function membership. The audit should sample high-risk workspaces and confirm that access aligns to documented project roles.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 17 access control matrix would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.