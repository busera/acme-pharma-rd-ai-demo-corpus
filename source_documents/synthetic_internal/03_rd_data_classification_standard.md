# R&D Data Classification Standard

**Record owner:** R&D Data Council
**Approver:** Quality and Regulatory Science; Privacy; Security
**Status:** Version 1.1, effective
**Effective or as-of date:** 15 March 2026
**Review cycle:** Annual

## Classification scheme

| Class | Example R&D content | AI handling rule |
|---|---|---|
| Public scientific information | Published papers, public patents, conference abstracts | Approved external tools may be used if licensing and citation rules are met |
| Internal research information | Target strategy, study rationales, non-public hypotheses | Approved ACME environment only; no vendor training or retention unless explicitly approved |
| Restricted research information | Unpublished results, compound structures, assay results, partner data | Segregated environment, access logging, project approval, data minimization |
| GxP or submission-support information | GLP study records, validated assay outputs, regulatory response sources | Use requires GxP Boundary Review, an assured workflow, audit trail, and retention rule |
| Personal or sensitive data | Researcher identifiers, coded subject data, collaborator personal data | Privacy impact review and minimum necessary processing required |

## Data-quality controls

AI workflows must preserve source identity, source version, extraction date, and transformation status. The standard requires users to flag when a source is incomplete, outdated, contradicted, or manually transcribed. For retrieval-based workflows, high-confidence output cannot rely on isolated passages only; users must check whether the broader document supports the generated statement.

The five classes are the only labels used in R&D AI intake and inventory records. Prompts, retrieved context, embeddings, generated summaries, reviewer feedback, exports, and support logs inherit the highest classification of their sources. A downgrade requires a documented decision approved by the data owner and R&D Data Council after redaction or aggregation has been verified.

## Practical handling expectations

For restricted research information, users may not paste content into unapproved external tools. Approved tools must document encryption, tenant isolation, retention period, support access, data residency, and whether prompts or outputs are used for training or service improvement. For GxP or submission-support information, the tool must have a documented intended use, access controls, audit trail expectations, backup and retention rationale, and quality review before output is relied on.
