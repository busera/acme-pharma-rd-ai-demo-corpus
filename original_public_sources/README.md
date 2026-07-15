# Original public-source files

This directory contains exact acquired copies of public-reference originals whose official reuse terms support redistribution. These files are included for provenance checking and reproducible source review.

## Important: not canonical scanner input

The canonical summary input is `source_documents/`, currently 55 Markdown files. This directory sits outside that scanner root deliberately. Ingesting both an original and its attributed public-reference record would duplicate and potentially overweight the same external authority.

Use the files here to:

- verify public-reference summaries and excerpts;
- reproduce source review against exact acquired bytes;
- inspect the original layout and context;
- compare future versions with the pinned acquisition.

Do not add this directory directly to an APM/AWP run. Use `scripts/prepare_corpus.py prepare-full`, which replaces all public-reference records with 20 originals and writes an adjacent corpus manifest.

## Integrity

`manifest.json` records each filename, byte count, SHA-256, official URL, reuse basis, and corresponding canonical corpus record. The copied bytes were verified against the reviewed Criteria Library acquisition before being committed.

## Reuse bases

- **FDA:** Unless otherwise noted, FDA website text and graphics are not copyrighted. Source: <https://www.fda.gov/about-fda/about-website/website-policies>
- **NIST:** NIST employee works are generally not subject to US copyright; NIST technical-series reuse is permitted with acknowledgement, subject to stated exceptions and foreign rights. Source: <https://www.nist.gov/open/license>
- **EMA:** EMA permits reproduction/distribution of EMA-published information with source acknowledgement, excluding third-party material and protected logos. Source: <https://www.ema.europa.eu/en/about-us/about-website/legal-notice>
- **EUR-Lex:** Legal documents may generally be reused for commercial or non-commercial purposes, subject to the EUR-Lex notice and third-party exclusions. Source: <https://eur-lex.europa.eu/content/legal-notice/legal-notice.html>
- **OWASP:** Unless otherwise specified, site content is licensed under Creative Commons Attribution-ShareAlike 4.0. Source: <https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/>
- **eCFR:** US federal regulatory text; the eCFR is continuously updated and authoritative but unofficial.

Logos, trademarks, third-party images, and third-party works retain their respective rights. No endorsement by an issuing authority is implied.

## Originals not redistributed

The following acquired originals are not committed because their file-level or publisher terms do not provide a sufficiently clear public-republication basis for this repository:

- AWS generative-AI data security page;
- AWS AI Security Scoping Matrix page;
- AWS Well-Architected Machine Learning Lens;
- OECD *Artificial Intelligence in Science*;
- OECD GLP Data Integrity advisory document;
- MHRA GxP Data Integrity guidance;
- ISPE GAMP 5 Second Edition publisher page.

Their attributed public-reference records, official URLs, and reviewed hashes remain in the canonical corpus and `FRAMEWORK_SOURCE_PROVENANCE.md`. `scripts/prepare_corpus.py fetch-restricted` downloads current official copies to a local cache and writes a receipt. Living HTML hashes are recorded but not compared; fixed-file changes are accepted and marked transparently.
