# Change Management Log for R&D AI Pilot

**Record owner:** NEURALIS Product Owner
**Approver:** R&D Digital Office Change Manager
**Status:** Working change log
**Effective or as-of date:** 30 June 2026
**Review cycle:** Per change

## Recent changes

| Date | Change | Reason | Approval status |
|---|---|---|---|
| 2026-03-05 | Added public literature corpus | support pilot testing | approved |
| 2026-03-12 | Added internal research summaries | improve relevance | pending Legal review |
| 2026-03-18 | Enabled vendor configuration support | implementation support | time-bound approval |
| 2026-03-22 | Modified retrieval settings | reduce irrelevant passages | technical approval only |
| 2026-03-29 | Added output review template | improve reviewer feedback | approved |

## Current constraint

Technical changes are logged, but the change process does not consistently identify whether a change affects legal, privacy, security, or scientific-integrity risk. For example, adding internal research summaries changes the data-risk profile more than the wording of the change entry suggests.

## Recent changes under review

| Change | Reason | Risk question |
|---|---|---|
| Added patent-search connector | Improve IP landscape support | Does connector terms-of-use permit the intended processing? |
| Updated retrieval weighting | Improve negative-evidence recall | Has regression testing shown no loss in source precision? |
| Enabled reviewer comments | Improve human review evidence | Are comments retained as controlled records or monitoring data? |
| Added external collaborator role | Support university partnership | Does access respect partner-data restrictions and exit obligations? |
| Expanded summary templates | Improve consistency | Are users mistaking templates for approved scientific conclusions? |



## Change categories

The change log tracks model endpoint changes, prompt-library updates, retrieval-source changes, user-interface changes, access-role changes, retention-setting changes, supplier subprocessor changes, and intended-use changes. Each change should identify whether re-evaluation is required. The log treats model upgrades as potentially material even where the application code is unchanged.

For R&D AI, a change can affect scientific interpretation without changing system availability. A new model may produce more confident language, different source selection, weaker uncertainty statements, or different ranking logic. Prompt-library changes may alter the boundary between drafting support and decision support. Retrieval-source changes may introduce outdated or unapproved records.
