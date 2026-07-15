# OWASP Top 10 for LLM Applications 2025

## Authority and status

- **Issuer:** OWASP GenAI Security Project
- **Edition:** 2025 release, published 18 November 2024
- **Status:** Community security guidance; nonbinding
- **License:** Creative Commons Attribution-ShareAlike 4.0
- **Official source:** <https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/>
- **Full report:** <https://genai.owasp.org/download/43299/?tmstv=1731900559>
- **Risk archive:** <https://genai.owasp.org/llm-top-10/>

This record summarizes the full 45-page 2025 report and supersedes the previous taxonomy.

## 2025 risk taxonomy

1. **LLM01:2025 Prompt Injection** — crafted or retrieved instructions can alter model behavior or connected actions.
2. **LLM02:2025 Sensitive Information Disclosure** — prompts, context, training data, or outputs may expose protected information.
3. **LLM03:2025 Supply Chain** — models, datasets, adapters, libraries, and service dependencies may introduce compromise or untracked change.
4. **LLM04:2025 Data and Model Poisoning** — manipulated training, fine-tuning, retrieval, or embedding data may corrupt behavior.
5. **LLM05:2025 Improper Output Handling** — unvalidated model output may trigger downstream injection, execution, or data-integrity failures.
6. **LLM06:2025 Excessive Agency** — broad permissions, tools, autonomy, or missing approvals can produce harmful actions.
7. **LLM07:2025 System Prompt Leakage** — exposed system instructions may reveal controls, sensitive context, or exploitable assumptions.
8. **LLM08:2025 Vector and Embedding Weaknesses** — retrieval and embedding systems may permit unauthorized access, poisoning, leakage, or cross-context contamination.
9. **LLM09:2025 Misinformation** — confident but false or misleading output can distort decisions and erode trust.
10. **LLM10:2025 Unbounded Consumption** — uncontrolled inference, context, loops, or requests can exhaust resources or create unexpected cost.

## Relevance to the ACME scenario

The taxonomy supports security and control questions for retrieval-augmented research assistants, external model endpoints, supplier components, embeddings, prompt libraries, generated outputs, and agent-like actions. It is particularly useful for assessing:

- prompt and retrieved-content trust boundaries;
- source, model, and supplier provenance;
- output validation before downstream reuse;
- least privilege and human approval for consequential actions;
- segregation and access controls for vector stores and embeddings;
- resource limits, monitoring, incident response, and change control.

## Use boundary

OWASP identifies application-security risks and mitigations. It is not law, pharmaceutical regulation, validation evidence, or proof that a specific vulnerability exists in ACME. Applicability must be evaluated against the actual architecture, data, intended use, and threat model.
