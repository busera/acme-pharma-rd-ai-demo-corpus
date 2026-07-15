# Model Development Lifecycle SOP for R&D AI

**Record owner:** R&D Digital Office
**Approver:** R&D AI Steering Committee
**Status:** Version 1.0, effective
**Effective or as-of date:** 1 April 2026
**Review cycle:** Annual

## Required artifacts

Each AI use case should maintain a use-case record, accountable owner, data classification, model or service description, data-flow diagram, validation plan, known limitations, human review procedure, third-party risk assessment, security review, and change log.

## R&D-specific additions

For research use, the record should also capture whether outputs influence hypothesis generation, candidate selection, experiment prioritization, regulatory evidence, patent decisions, or collaboration discussions.

## GxP trigger questions

A use case requires Quality assessment if model output is copied into a controlled record, supports a decision later used in a regulatory submission, changes acceptance criteria or experimental design, affects GxP data processing, or becomes part of a validated process. The SOP currently says this assessment is required, but it does not yet define who can make the final GxP classification when R&D, Quality, and Regulatory disagree.

## Eight-stage lifecycle

1. **Intake:** record the business problem, intended use, users, proposed data, decision impact, and supplier involvement.
2. **Classification:** assign risk based on intended use, data, decision impact, GxP relevance, personal or sensitive data, and supplier involvement.
3. **Design:** define allowed inputs, output boundaries, human review, architecture, records, and acceptance criteria.
4. **Build/configure:** implement the model, prompts, retrieval, interfaces, access controls, and supplier components under change control.
5. **Evaluate:** test scientific utility, traceability, failure modes, security, privacy, and proportionate assurance requirements.
6. **Release:** approve the stated use, user group, data boundary, training, support, and monitoring plan.
7. **Monitor/change:** review usage, performance, incidents, feedback, drift, supplier changes, and material changes before deployment.
8. **Retire:** remove access, preserve required records, delete data and derived artifacts, and close inventory entries.

Assurance scales with intended use, data classification, decision impact, GxP relevance, and supplier involvement. A stage may be repeated when the scope changes, but none may be omitted without a documented exception approved by the R&D AI Steering Committee.

## Change and retirement expectations

The SOP requires a change record when the model, retrieval corpus, prompt library, user group, intended use, data class, or supplier access changes materially. A model upgrade is not treated as a routine patch if it changes behavior for a decision-support workflow. Retirement must include user notification, data export or deletion, revoked access, archive of validation evidence, and confirmation that downstream records remain understandable.
