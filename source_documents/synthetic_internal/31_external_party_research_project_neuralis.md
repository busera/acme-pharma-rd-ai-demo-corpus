# Project NEURALIS external-party R&D AI co-development charter

**Record owner:** NEURALIS Project Manager
**Approver:** Translational Medicine Business Owner and R&D Digital Office Product Owner
**Status:** Version 0.9, controlled development
**Effective or as-of date:** 30 June 2026
**Review cycle:** Monthly

## Project summary

Project NEURALIS is developing an AI-supported research-assistant workflow for translational medicine teams. The solution helps scientists compare public literature, summarize internal research context, identify contradictory evidence, and challenge proposed experiment designs before a protocol is finalized.

The solution is being co-developed with HelixBridge Analytics, an external analytics and AI engineering partner. HelixBridge provides implementation support, evaluation design, retrieval tuning, interface configuration, and model-monitoring advice. ACME Pharma owns the scientific intended use, source-data approval, output review, risk acceptance, and decision to expand beyond development.

## Current project status

|---|---|---|
| Business case | Approved for controlled development | Value case is clear, but risk appetite for broader rollout is not documented |
| Technical build | Prototype in controlled development workspace | Architecture review is not final |
| Data use | Public scientific information plus selected restricted internal summaries | Upload enforcement and deletion evidence are not yet proven |
| Supplier role | HelixBridge performs build and tuning support | Shared-responsibility boundaries need clearer evidence |
| GxP boundary | Initial view says not GxP, but outputs may influence protocol design | Quality and Regulatory Science have not issued final classification |
| Validation | Test approach drafted | Negative-evidence and contradictory-source tests are immature |
| IP and ownership | Main deliverables assigned to ACME Pharma | Derived artifacts are not fully named in contract annex |
| Exit | Draft exit checklist exists | Embeddings, evaluation cases, support tickets, and backups need explicit handling |

## Parties and responsibilities

| Party | Role | Responsibility boundary |
|---|---|---|
| ACME Pharma Translational Medicine | Business owner | Defines intended use, reviewer process, scientific decision boundaries, and expansion criteria |
| ACME Pharma R&D Digital Office | Product owner | Owns roadmap, user access, release readiness, support model, and inventory entries |
| ACME Pharma R&D Data Council delegate | Data owner delegate | Approves source data classes, retention, deletion, and lineage expectations |
| ACME Pharma Quality and Regulatory Science | GxP boundary owner | Determines whether output affects controlled records, submission support, or validation scope |
| ACME Pharma Legal/IP | Legal owner | Reviews ownership, no-training, reuse, confidentiality, invention-support, and exit terms |
| ACME Pharma TPRM / Procurement | Supplier control owner | Performs vendor due diligence and monitors supplier obligations |
| HelixBridge Analytics | External co-development partner | Builds and tunes the workflow under ACME-approved data, access, and reuse restrictions |

## AI artifacts created by the project

- Use-case description and intended-use statement.
- Source-document classification rules.
- Retrieval configuration and evaluation cases.
- Prompt and instruction patterns for experiment-design challenge.
- Embeddings and search index derived from approved source material.
- Reviewer feedback and output disposition records.
- Model-behavior test reports and failure examples.
- Monitoring dashboard definitions.
- Workflow documentation and training material.

## Open co-development questions

1. Can HelixBridge use anonymized prompts, output ratings, error reports, support tickets, or evaluation results for service improvement?
2. Who owns retrieval configuration, prompts, evaluation cases, embeddings, and reviewer-feedback datasets?
3. Can HelixBridge reuse generalized design patterns learned from ACME Pharma's R&D workflow with other clients?
4. Which subcontractors can access logs, source extracts, embeddings, or support tickets?
5. What evidence proves deletion of source material and derived artifacts at project exit?
6. What change by HelixBridge requires ACME Pharma retesting and approval?
7. If AI output changes an experiment-design decision, how is that captured in the scientific record?
8. If Quality later classifies the workflow as GxP-relevant, what additional validation and record controls are required?

## Project workstreams

Project NEURALIS has four workstreams. Workstream A designs retrieval and summarization over approved literature and internal research notes. Workstream B develops experiment-design challenge prompts and evaluation examples. Workstream C builds reviewer feedback capture and issue tracking. Workstream D prepares governance evidence for any future expansion beyond sandbox use. The supplier contributes workflow design and technical implementation; ACME contributes scientific requirements, review examples, and acceptance criteria.

The project plan states that NEURALIS is not approved for regulatory submission support, automated candidate advancement, protocol approval, or GxP record generation. It may support research discussions if outputs remain draft, source-linked, and reviewed by accountable scientists. The unresolved question is whether repeated use in candidate-review preparation turns the tool into decision support requiring stronger assurance.

## Co-development risks under review

The project creates artifacts that are more sensitive than ordinary deliverables: prompt patterns, evaluation examples, reviewer comments, defect labels, acceptance criteria, and source-selection rules. These artifacts can reveal how ACME evaluates research uncertainty. Legal/IP has asked for clear ownership and reuse restrictions. Security has asked for support-access logging. Quality has asked for a boundary assessment before any output enters controlled records.
