# ACME Pharma AI governance operating model

**Record owner:** Enterprise AI Governance Office
**Approver:** R&D AI Steering Committee
**Status:** Version 1.0, effective
**Effective or as-of date:** 1 March 2026
**Review cycle:** Annual

## Governance concept

ACME Pharma treats AI governance as a lifecycle control system, not a policy page. The governance model covers how AI ideas are proposed, classified, built, approved, monitored, changed, expanded, and retired. The R&D AI portfolio must be visible through two linked registers:

1. AI use-case inventory: the business purpose, user group, intended decision impact, data class, and process context.
2. AI system inventory: the technical solution, model type, data flow, supplier dependencies, lifecycle state, controls, and monitoring evidence.


## Governance principles

| Principle | Practical meaning for R&D AI |
|---|---|
| Human accountability | AI may support analysis, challenge, drafting, and comparison, but named ACME Pharma scientists or process owners remain accountable for decisions. |
| Intended-use clarity | Every use case must state what the AI output may and may not be used for. |
| Risk-based assurance | Testing, validation, review, and documentation scale with data sensitivity, decision impact, GxP relevance, and external-party exposure. |
| Source traceability | Material claims, summaries, rankings, and recommendations must be traceable to source material and reviewer judgment. |
| Data minimization | Data used in AI workflows must be approved, necessary, classified, and retained only as long as justified. |
| Supplier accountability | External parties may provide tools or support, but ACME Pharma retains accountability for intended use, data approval, scientific interpretation, regulated records, and risk acceptance. |
| Change control | Model, prompt, retrieval, data-source, workflow, vendor, or configuration changes require impact assessment and proportionate retesting. |
| Continuous monitoring | High-impact systems need monitoring for performance drift, source-quality issues, blocked requests, incidents, and user behavior. |

## Governance forums and decision rights

| Decision | Primary forum | Required input |
|---|---|---|
| New AI idea accepted into intake | Enterprise AI Governance Office | Use-case owner, business rationale, expected data classes, supplier involvement |
| R&D pilot prioritized | R&D AI Steering Committee | R&D value case, user group, intended decision impact, resource request |
| GxP or electronic-record boundary set | GxP Boundary Review | Quality, Regulatory Science, system owner, data steward, process owner |
| External party/co-development accepted | Supplier Co-Development Review | Legal/IP, TPRM, Procurement, Privacy, Security, business owner |
| Sandbox-to-controlled-use promotion | Enterprise AI Governance Office and R&D AI Steering Committee | Test evidence, monitoring plan, training, support model, residual-risk acceptance |
| Production or GxP-relevant use approved | Quality and Regulatory Science with AI Governance | Validation/assurance package, audit trail, change control, controlled-record handling |
| Material incident escalated | AI Incident Triage Group | Security, Privacy, Legal, Quality, business owner, supplier contact if applicable |

## Lifecycle decision points

Governance decisions follow the eight stages defined in the lifecycle SOP: intake, classification, design, build/configure, evaluate, release, monitor/change, and retire. Required review depth scales with intended use, data, decision impact, GxP relevance, and supplier involvement.

## Risk-tiering logic

| Tier | Typical R&D AI use | Minimum governance expectation |
|---|---|---|
| Tier 1 | Public literature summarization, meeting preparation, glossary support | Inventory entry, approved tool, user training, citation review |
| Tier 2 | Internal research synthesis, experiment-design challenge, patent landscape support | Data approval, output review, source traceability, supplier checks, monitoring |
| Tier 3 | Candidate prioritization, protocol-design support, lab-note synthesis | Formal risk assessment, stronger validation/assurance, Quality and Regulatory Science review, audit trail review |
| Tier 4 | GxP-relevant records, submission-support content, automated decision support | Controlled lifecycle, Part 11/GxP assessment, validation package, strict change control, formal approval |

## Current operating constraints

- AI use-case inventory and AI system inventory are not fully reconciled.
- Some use cases are classified by tool owner rather than intended use and decision impact.
- Supplier co-development controls are stronger for source data than for derived artifacts such as prompts, embeddings, evaluation sets, and configuration patterns.
- GxP boundary review is documented for obvious regulated records, but less clear for research outputs that later influence submission-support decisions.
- Monitoring focuses on application usage and blocked requests; it does not yet consistently monitor source-quality failures, negative-evidence misses, or reviewer overreliance.



## Governance decision rights

The governance model assigns decision rights across four levels. Enterprise AI Governance defines minimum principles, risk-tiering, and inventory requirements. R&D AI Steering Committee interprets those principles for research workflows and approves high-risk pilots. System owners operate technical controls and lifecycle evidence. Business owners accept intended use, output review, and scientific accountability. No single approval is sufficient where a use case crosses data, supplier, GxP, and decision-impact boundaries.

Governance requires two linked inventories. The AI use-case inventory explains the business activity and decision impact. The AI system inventory explains the technical service, platform, model endpoint, data stores, and operational owner. A use case without a system record may hide technical risk. A system without use-case records may hide uncontrolled business expansion.

## Escalation conditions

The model names five failure modes: undocumented shadow AI, inventory mismatch, pilot drift into production, supplier reuse of derived artifacts, and unclear GxP boundary. Each failure mode has expected control evidence. For shadow AI, evidence includes survey follow-up and approved alternatives. For inventory mismatch, evidence includes reconciliation. For pilot drift, evidence includes time-boxed approvals and monitoring. For supplier reuse, evidence includes contract clauses and retained-artifact review. For GxP boundary, evidence includes intended-use assessment and Quality sign-off.
