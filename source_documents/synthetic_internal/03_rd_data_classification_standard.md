---
title: R&D Data Classification Standard
doc_type: policy
owner: Information Governance
status: approved
company: ACME Pharma
confidentiality: Internal
scenario: AI in Research and Development planning evidence
Document_File_Name: 03_rd_data_classification_standard.md
IIA_Type: GOV
IIA_Type_Rational: This document is an internal policy that establishes data classification
  categories and AI handling rules, serving as a governance framework for R&D AI pilots.
  It defines controls and requirements, making it a governance document.
Quality_Rating: H
Relevance_Score: H
Fact: 'The standard defines five R&D data classes: public scientific information,
  internal research context, confidential research data, restricted trade-secret material,
  and regulated personal or clinical data. AI handling rules require that public information
  may be processed by approved tools with copyright and license respect; internal
  context only in approved enterprise tools; confidential and trade-secret data require
  documented business owner approval, legal review for third-party processing, and
  technical controls preventing vendor training or uncontrolled retention; regulated
  personal data requires privacy review and lawful basis. A known gap is that embeddings
  derived from restricted research text are not yet classified, raising questions
  about vector databases, retrieval indexes, cache layers, and vendor telemetry. The
  standard also includes a table with additional classes such as GxP or submission-relevant
  records, which require Quality/Regulatory assessment, validated or assured workflow,
  audit trail, and retention rules. Data-quality controls mandate that AI workflows
  preserve source identity, source version, extraction date, and transformation status,
  and require users to flag sources that are incomplete, outdated, or contradicted.'
Summary: 'The R&D Data Classification Standard is an approved internal policy that
  categorizes ACME Pharma''s research and development data into five classes: public
  scientific information, internal research context, confidential research data, restricted
  trade-secret material, and regulated personal or clinical data. For each class,
  it prescribes specific AI handling rules. Public scientific information may be processed
  by approved external AI tools provided copyright and license terms are respected.
  Internal research context is restricted to approved enterprise tools only. Confidential
  research data and trade-secret material require documented business owner approval,
  legal review when third-party processing is involved, and technical controls that
  prevent vendor training or uncontrolled retention. Regulated personal or clinical
  data necessitates a privacy review and an explicit lawful basis for processing.
  The standard also identifies a known gap: it does not define whether embeddings
  derived from restricted research text inherit the same classification, which creates
  uncertainty for vector databases, retrieval indexes, cache layers, and vendor telemetry.
  Additionally, a table extends the classification to include GxP or submission-relevant
  records, which demand Quality/Regulatory assessment, validated or assured workflows,
  audit trails, and retention rules. Data-quality controls are specified, requiring
  AI workflows to preserve source identity, version, extraction date, and transformation
  status, and obligating users to flag sources that are incomplete, outdated, or contradicted.
  The document serves as a governance baseline for AI use in R&D.'
Section_Context: Governance framework
IIA_Relevance_Explanation: This document is an internal policy that establishes data
  classification categories and AI handling rules, serving as a governance framework
  for R&D AI pilots. It defines controls and requirements, making it a governa...
IIA_Relevance: H
IIA_Confidence: H
Notes: 'Auto-derived categorization: This document is an internal policy that establishes
  data classification categories and AI handling rules, serving as a governance framework
  for R&D AI pilot...'
---

# R&D Data Classification Standard


## R&D data classes

- Public scientific information: published papers, public patents, conference abstracts, public standards.
- Internal research context: project plans, experiment designs, internal literature notes, early hypotheses.
- Confidential research data: lab notebooks, assay results, compound or material properties, unpublished findings, negative results, protocol deviations.
- Restricted trade-secret material: proprietary methods, candidate selection rationale, formulation details, unique experimental workflows, model features derived from internal know-how.
- Regulated personal or clinical data: any human-subject, patient, employee, or identifiable contributor data.

## AI handling rules

Public scientific information may be processed by approved AI tools when copyright and license terms are respected. Internal research context may only be processed in approved enterprise tools. Confidential research data and trade-secret material require a documented business owner approval, legal review for third-party processing, and technical controls that prevent vendor training or uncontrolled retention. Regulated personal or clinical data requires privacy review and explicit lawful basis.

## Known gap

The current standard does not yet define whether embeddings derived from restricted research text inherit the same classification as the source. For audit planning, this creates a question about vector databases, retrieval indexes, cache layers, and vendor telemetry.

## ACME Pharma R&D data classes for AI use

| Class | Example R&D content | AI handling rule |
|---|---|---|
| Public scientific information | Published papers, public patents, conference abstracts | Approved external tools may be used if licensing and citation rules are met |
| Internal research context | Target strategy, study rationales, non-public hypotheses | Approved ACME environment only; no vendor training or retention unless explicitly approved |
| Restricted research data | Unpublished results, compound structures, assay results, partner data | Segregated environment, access logging, project approval, data minimization |
| GxP or submission-relevant records | GLP study records, validated assay outputs, regulatory response sources | Use requires Quality/Regulatory assessment, validated or assured workflow, audit trail, retention rule |
| Personal or sensitive data | Researcher identifiers, coded subject data, collaborator personal data | Privacy impact review and minimum necessary processing required |

## Data-quality controls

AI workflows must preserve source identity, source version, extraction date, and transformation status. The standard requires users to flag when a source is incomplete, outdated, contradicted, or manually transcribed. For retrieval-based workflows, high-confidence output cannot rely on isolated passages only; users must check whether the broader document supports the generated statement.

## Data classes relevant to R&D AI

The R&D data standard uses four practical classes for AI intake decisions. Public scientific information includes publications, conference abstracts, public patents, public trial registry data, and open regulatory guidance. Internal research information includes internal summaries, working hypotheses, target-selection rationale, portfolio notes, and unpublished experimental context. Restricted research information includes proprietary assay results, preclinical findings, coded study data, partner-confidential material, trade-secret protocols, and candidate prioritization rationale. Controlled GxP or submission-support information includes validated evidence packs, electronic records used to support development decisions, inspection-relevant records, and draft regulatory responses based on approved source material.

The standard requires teams to classify not only the input data but also prompts, retrieved context, embeddings, generated summaries, reviewer feedback, exported files, and support logs. This is an important distinction for AI systems because the sensitive material may appear in derived artifacts even where the original document is not stored in the AI tool. The data owner must decide whether those derived artifacts inherit the highest source classification or can be downgraded after redaction and review.

## Practical handling expectations

For restricted research information, users may not paste content into unapproved external tools. Approved tools must document encryption, tenant isolation, retention period, support access, data residency, and whether prompts or outputs are used for training or service improvement. For GxP or submission-support information, the tool must have a documented intended use, access controls, audit trail expectations, backup and retention rationale, and quality review before output is relied on.

The standard also flags coded human subject data and clinical-adjacent data as special cases. Even where direct identifiers are absent, research context can make records sensitive. Teams must consult Privacy before using patient-derived, genomic, biomarker, pharmacovigilance-adjacent, or externally sourced data in AI workflows. The audit should test whether this privacy trigger is understood by project teams and reflected in intake records.

## Detailed audit scenario and sample evidence

For audit planning, this artifact would normally be supported by several underlying records rather than read in isolation. Expected supporting evidence includes the accountable owner, approval date, related use-case ID, related system ID, affected R&D functions, data classes permitted, supplier involvement, intended decision impact, and the operating procedure or workflow that tells users what to do. A mature record would also show exceptions, issue follow-up, and the date when the artifact was last challenged by governance.

A realistic sample for 03 rd data classification standard would include at least one discovery-science workspace, one translational-science workspace, and one regulatory-science or quality-adjacent scenario. The sample should show whether the same rule is applied differently depending on data class. Public literature summaries should have lighter evidence requirements. Restricted research content should require project-owner approval, traceability to source material, and explicit output-review responsibility. GxP-adjacent or submission-support use should require a documented boundary assessment and stronger change-control evidence.

The most useful audit evidence is not the existence of the document itself. It is the join between this document and operating records: inventory entries, project approvals, access groups, supplier clauses, monitoring logs, training completion, and examples of outputs reviewed or rejected. If those joins cannot be shown, the control may exist on paper but not operate reliably.

## Questions for walkthroughs

During walkthroughs, the audit team should ask who owns this artifact, how teams know when it applies, what happens when a pilot changes scope, where exceptions are logged, and how management knows the artifact is being followed. The team should also ask for one example where the rule stopped or changed a proposed AI use. Evidence of a controlled rejection, redesign, or escalation is often a stronger sign of governance maturity than a list of approved pilots.