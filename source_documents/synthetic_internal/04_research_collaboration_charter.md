---
title: Research Collaboration Charter for AI-Enabled Projects
doc_type: charter
owner: R&D Partnerships
status: draft
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 04_research_collaboration_charter.md
IIA_Type: GOV
IIA_Type_Rational: The document is a charter that establishes governance structures,
  roles, responsibilities, and required controls for AI research collaborations, aligning
  with IIA's governance documentation type.
Quality_Rating: M
Relevance_Score: H
Fact: 'The charter defines collaboration types: advisory support, data processing,
  tool configuration, model evaluation, model co-development, and joint research.
  Each collaboration must define data shared, outputs created, ownership, reuse, personnel
  access, and post-engagement handling. Subcontracting must be disclosed and approved.
  Co-development clauses cover ownership of model artifacts, prompts, evaluation datasets,
  embeddings, code, and documentation; restrictions on partner use of project learnings;
  audit rights; exit support; and data destruction. Roles include research sponsor,
  scientific product owner, data steward, model owner, supplier technical lead, Quality,
  Legal/IP, Privacy, Security, and Internal Audit observer. ACME retains accountability
  for intended use, source-data approval, scientific interpretation, regulated records,
  and expansion decisions. Joint work products must be listed in a collaboration asset
  register with ownership and reuse restrictions. Project NEURALIS is a test case
  for the collaboration model with HelixBridge Analytics. The planning note states
  Legal and Third Party Risk Management own contractual interpretation, and Internal
  Audit should verify assessments happened and risk owners understand residual exposure.'
Summary: The Research Collaboration Charter for AI-Enabled Projects defines how ACME
  Pharma R&D collaborates with universities, contract research organizations, analytics
  vendors, and AI implementation partners. It specifies required controls for each
  collaboration, including data sharing, output ownership, reuse rights, personnel
  access, and post-engagement obligations, with subcontracting requiring disclosure
  and approval. The charter details co-development clauses to confirm, such as ownership
  of model artifacts, prompts, evaluation datasets, embeddings, code, and documentation,
  as well as restrictions on partner use of learnings, audit rights, exit support,
  and data destruction. It assigns clear roles and responsibilities, with ACME retaining
  accountability for scientific use, data handling, and regulatory decisions, while
  suppliers handle technical configuration. A shared-responsibility boundary is established,
  and joint work products must be recorded in a collaboration asset register with
  ownership and reuse restrictions. The document notes that Legal and Third Party
  Risk Management own contractual interpretation, and Internal Audit should verify
  that proper assessments occurred and risk owners understand residual exposure. Project
  NEURALIS, a co-developed R&D AI assistant with HelixBridge Analytics, is identified
  as a test case for the collaboration model. The charter is in draft status and is
  internal to ACME Pharma.
Section_Context: Governance framework
IIA_Relevance_Explanation: The document is a charter that establishes governance structures,
  roles, responsibilities, and required controls for AI research collaborations, aligning
  with IIA's governance documentation type.
IIA_Relevance: H
IIA_Confidence: M
Notes: 'Auto-derived categorization: The document is a charter that establishes governance
  structures, roles, responsibilities, and required controls for AI research collaborations,
  aligning wit...'
---

# Research Collaboration Charter for AI-Enabled Projects


## Collaboration model

ACME Pharma R&D collaborates with universities, contract research organizations, analytics vendors, and specialist AI implementation partners. The charter defines collaboration types: advisory support, data processing, tool configuration, model evaluation, model co-development, and joint research.

## Required controls

Each collaboration must define what data is shared, what outputs are created, who owns the outputs, who may reuse the learnings, which personnel may access the material, and what happens after the engagement ends. Subcontracting must be disclosed and approved before access is granted.

## Co-development clauses to confirm

- Ownership of model artifacts, prompts, evaluation datasets, embeddings, code, and documentation.
- Whether the partner may use project learnings for other customers or internal model improvement.
- Whether the partner may train, fine-tune, benchmark, or improve models using company material.
- Audit rights and evidence expectations for access logs, deletion, data segregation, and security controls.
- Exit support, portability, and secure destruction or return of data.

## Planning note

Legal and Third Party Risk Management own contractual interpretation. Internal Audit should not provide legal conclusions, but should verify that the right assessments happened and that R&D risk owners understand residual exposure.

## Collaboration model

ACME Pharma separates collaboration roles into research sponsor, scientific product owner, data steward, model owner, supplier technical lead, Quality representative, Legal/IP counsel, Privacy, Security, and Internal Audit observer. The charter requires one accountable ACME owner for scientific use, one accountable ACME owner for data handling, and one accountable supplier contact for technical changes.

## Shared-responsibility boundaries

The supplier may configure pipelines, assist with evaluation design, and support model adaptation, but ACME retains accountability for intended use, source-data approval, scientific interpretation, regulated records, and decisions to expand use. Joint work products such as prompts, evaluation sets, benchmark results, embeddings, adapters, and workflow documentation must be listed in a collaboration asset register with ownership and reuse restrictions.

## External-party project example

Project NEURALIS is the current test case for the collaboration model. It involves a co-developed R&D AI assistant with HelixBridge Analytics and should be used to test whether shared responsibility, derived-artifact ownership, no-training restrictions, support access, GxP boundary review, and exit obligations are more than policy language.

## Collaboration governance model

The collaboration charter requires every AI-enabled research collaboration to identify the scientific objective, the external party's role, expected data flows, model ownership assumptions, and the accountable ACME decision owner. The charter is intended to prevent a common failure mode: the science team treats the external party as a research collaborator, Procurement treats the party as a technology supplier, and Legal treats the AI artifacts as ordinary deliverables. For AI co-development, all three views are incomplete unless they are joined.

The charter distinguishes four collaboration patterns. A tool-use arrangement gives ACME access to a third-party AI product. A service arrangement asks the third party to run AI-enabled analysis on ACME data. A co-development arrangement creates prompts, models, evaluation sets, or workflows jointly. A research partnership may create methods and scientific outputs where ownership, publication rights, and confidentiality need separate handling. Each pattern has different risks around training data, reuse of know-how, derived artifacts, and exit.

## Required evidence before project start

Before project kickoff, the sponsor must document the intended use, data classes, expected outputs, human review points, publication expectations, IP ownership, subcontractor access, model-training restrictions, support-log retention, and deletion evidence. The charter also requires a "no silent reuse" clause: the external party may not reuse prompts, embeddings, reviewer feedback, evaluation examples, or ACME-derived workflows for unrelated clients or product improvement unless a specific written exception is approved.

The audit should test whether collaboration charters are created before work begins, not retrofitted after the first data transfer. Evidence should include steering approval, legal review, privacy screening, security assessment, data-transfer instructions, and a named scientific accountable owner.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 04 research collaboration charter would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.