# Access Control Matrix for R&D AI Sandbox

**Record owner:** NEURALIS Product Owner
**Approver:** Security
**Status:** Version 0.7, controlled development
**Effective or as-of date:** 10 June 2026
**Review cycle:** Quarterly and at role change

## Roles

| Role | Main permissions | Review requirement |
|---|---|---|
| Pilot Researcher | Ask questions against approved project corpus | manager approval |
| Principal Scientist | Approve experiment-design use | R&D leadership approval |
| R&D AI Product Owner | Manage use-case record and user access | quarterly access review |
| Support Engineer | Troubleshoot application layer | break-glass or ticketed access |
| Vendor Specialist | Limited configuration support | Legal/TPRM approval and time-bound account |

## Control expectations

Access should be least privilege, time-bound for external personnel, logged, and reviewed periodically. Shared accounts are not permitted. Vendor support must not access research content unless explicitly approved.

## Open action

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
| Quality and Regulatory Science reviewer | GxP assessment package and controlled evidence | Read-only unless assigned approver role |

## Access weaknesses

Current evidence shows strong identity federation but weaker evidence around supplier break-glass access, dormant collaborators, and whether privileged users can view restricted prompts or outputs outside the application review workflow.

## Role model

The access model defines separate roles for viewer, researcher, project owner, data steward, system administrator, supplier support, and governance reviewer. Researchers can query approved workspaces but cannot change retention settings, supplier configuration, or model endpoints. Project owners can approve workspace membership and export outputs. Data stewards approve data-classification decisions and source-corpus changes. System administrators manage platform configuration but should not routinely access research content.

Supplier support access is treated as privileged and time-bound. The matrix requires named approval, reason for access, scope, start and end time, logging, and post-access review. Emergency access must be reviewed after the fact. Shared support accounts are not permitted.
