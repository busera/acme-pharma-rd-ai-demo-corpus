---
title: ACME Pharma AI governance operating model
company: ACME Pharma
doc_type: governance framework
owner: Enterprise AI Governance Office
status: approved for pilot governance
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 30_ai_governance_operating_model.md
IIA_Type: GOV
IIA_Type_Rational: The document defines the AI governance operating model, including
  principles, decision rights, and lifecycle controls, directly addressing the governance
  and control environment for AI pilots.
Quality_Rating: H
Relevance_Score: H
Fact: 'The governance model treats AI governance as a lifecycle control system covering
  proposal, classification, building, approval, monitoring, change, expansion, and
  retirement. The R&D AI portfolio must be visible through two linked registers: an
  AI use-case inventory and an AI system inventory. The human accountability principle
  states that named ACME Pharma scientists or process owners remain accountable for
  decisions even when AI supports analysis. Intended-use clarity requires every use
  case to state what the AI output may and may not be used for. Risk-based assurance
  scales testing, validation, review, and documentation with data sensitivity, decision
  impact, GxP relevance, and external-party exposure. Source traceability mandates
  that material claims, summaries, rankings, and recommendations be traceable to source
  material and reviewer judgment. Change control requires impact assessment and proportionate
  retesting for model, prompt, retrieval, data-source, workflow, vendor, or configuration
  changes. Governance forums include the AI Governance Review Board for new AI ideas,
  the R&D AI Steering Committee for pilot prioritization, and the GxP Boundary Review
  for setting GxP or electronic-record boundaries.'
Summary: 'The document presents ACME Pharma''s AI governance operating model as a
  lifecycle control system rather than a static policy. It requires the R&D AI portfolio
  to be tracked through two interconnected registers: one for use cases and one for
  systems, enabling audit to test both business and technical perspectives. Seven
  governance principles are defined: human accountability, intended-use clarity, risk-based
  assurance, source traceability, data minimization, supplier accountability, and
  change control. Each principle is translated into practical meaning for R&D AI,
  such as ensuring named scientists remain accountable and that AI outputs have clear
  permitted uses. The model establishes specific governance forums with decision rights:
  the AI Governance Review Board accepts new AI ideas, the R&D AI Steering Committee
  prioritizes pilots, and the GxP Boundary Review determines GxP or electronic-record
  boundaries. Required inputs for each decision are outlined, linking use-case owners,
  business rationale, data classes, and supplier involvement. The framework emphasizes
  that ACME Pharma retains accountability for intended use, data approval, scientific
  interpretation, and risk acceptance even when external parties provide tools or
  support. Continuous monitoring is required for high-impact systems to detect performance
  drift, source-quality issues, and incidents. The document is approved for pilot
  governance and serves as the foundational governance structure for AI initiatives
  in R&D.'
Section_Context: Governance framework
IIA_Relevance_Explanation: The document defines the AI governance operating model,
  including principles, decision rights, and lifecycle controls, directly addressing
  the governance and control environment for AI pilots.
IIA_Relevance: H
IIA_Confidence: H
Notes: 'Auto-derived categorization: The document defines the AI governance operating
  model, including principles, decision rights, and lifecycle controls, directly addressing
  the governance and...'
---

# ACME Pharma AI governance operating model

## Governance concept

ACME Pharma treats AI governance as a lifecycle control system, not a policy page. The governance model covers how AI ideas are proposed, classified, built, approved, monitored, changed, expanded, and retired. The R&D AI portfolio must be visible through two linked registers:

1. AI use-case inventory: the business purpose, user group, intended decision impact, data class, and process context.
2. AI system inventory: the technical solution, model type, data flow, supplier dependencies, lifecycle state, controls, and monitoring evidence.

One AI system can support several use cases. One use case can also depend on several AI systems. Audit should test both views because business owners often understand use cases, while technology and control owners manage systems.

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
| New AI idea accepted into intake | AI Governance Review Board | Use-case owner, business rationale, expected data classes, supplier involvement |
| R&D pilot prioritized | R&D AI Steering Committee | R&D value case, user group, intended decision impact, resource request |
| GxP or electronic-record boundary set | GxP Boundary Review | Quality, Regulatory Science, system owner, data steward, process owner |
| External party/co-development accepted | Supplier Co-Development Review | Legal/IP, TPRM, Procurement, Privacy, Security, business owner |
| Sandbox-to-controlled-use promotion | AI Governance Review Board and R&D AI Steering Committee | Test evidence, monitoring plan, training, support model, residual-risk acceptance |
| Production or GxP-relevant use approved | Quality / Regulatory Science with AI Governance | Validation/assurance package, audit trail, change control, controlled-record handling |
| Material incident escalated | AI Incident Triage Group | Security, Privacy, Legal, Quality, business owner, supplier contact if applicable |

## Lifecycle gates

1. Intake and inventory entry.
2. Intended-use and user-group definition.
3. Data classification and privacy review.
4. Supplier and co-development assessment.
5. GxP / Part 11 / submission-support boundary review.
6. Design and documentation review.
7. Test and assurance plan approval.
8. Pilot release approval.
9. Monitoring and reviewer-feedback review.
10. Expansion, restriction, or retirement decision.

## Risk-tiering logic

| Tier | Typical R&D AI use | Minimum governance expectation |
|---|---|---|
| Tier 1 | Public literature summarization, meeting preparation, glossary support | Inventory entry, approved tool, user training, citation review |
| Tier 2 | Internal research synthesis, experiment-design challenge, patent landscape support | Data approval, output review, source traceability, supplier checks, monitoring |
| Tier 3 | Candidate prioritization, protocol-design support, lab-note synthesis | Formal risk assessment, stronger validation/assurance, Quality/Regulatory review, audit trail review |
| Tier 4 | GxP-relevant records, submission-support content, automated decision support | Controlled lifecycle, Part 11/GxP assessment, validation package, strict change control, formal approval |

## Governance weaknesses already visible

- AI use-case inventory and AI system inventory are not fully reconciled.
- Some use cases are classified by tool owner rather than intended use and decision impact.
- Supplier co-development controls are stronger for source data than for derived artifacts such as prompts, embeddings, evaluation sets, and configuration patterns.
- GxP boundary review is documented for obvious regulated records, but less clear for research outputs that later influence submission-support decisions.
- Monitoring focuses on application usage and blocked requests; it does not yet consistently monitor source-quality failures, negative-evidence misses, or reviewer overreliance.

## Risk anchors for planning

The audit should treat the governance model as a way to test risk coverage, not as proof of control effectiveness. Relevant risk anchors include missing AI inventory, inadequate AI governance framework, lack of clear accountability, unmanaged AI acquisition and use, AI supply chain and third-party risk, sensitive data disclosure and inference, inadequate system documentation, ineffective AI change management, inadequate verification and validation, continuous validation failure, metadata and lineage management failure, insufficient logging and forensics, and improper decommissioning.

## Governance decision rights

The governance model assigns decision rights across four levels. Enterprise AI Governance defines minimum principles, risk-tiering, and inventory requirements. R&D AI Steering interprets those principles for research workflows and approves high-risk pilots. System owners operate technical controls and lifecycle evidence. Business owners accept intended use, output review, and scientific accountability. No single approval is sufficient where a use case crosses data, supplier, GxP, and decision-impact boundaries.

Governance requires two linked inventories. The AI use-case inventory explains the business activity and decision impact. The AI system inventory explains the technical service, platform, model endpoint, data stores, and operational owner. A use case without a system record may hide technical risk. A system without use-case records may hide uncontrolled business expansion.

## Control failure modes

The model names five failure modes: undocumented shadow AI, inventory mismatch, pilot drift into production, supplier reuse of derived artifacts, and unclear GxP boundary. Each failure mode has expected control evidence. For shadow AI, evidence includes survey follow-up and approved alternatives. For inventory mismatch, evidence includes reconciliation. For pilot drift, evidence includes time-boxed approvals and monitoring. For supplier reuse, evidence includes contract clauses and retained-artifact review. For GxP boundary, evidence includes intended-use assessment and Quality sign-off.

The audit should test whether governance decisions are evidenced at the moment of transition. The important moments are intake, first restricted-data use, supplier onboarding, pilot start, model change, output reuse in decision material, and production expansion.