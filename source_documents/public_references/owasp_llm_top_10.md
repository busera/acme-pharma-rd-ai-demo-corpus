---
Document_File_Name: owasp_llm_top_10.md
IIA_Type: REG
IIA_Type_Rational: The OWASP Top 10 for LLM Applications is an industry-recognized
  standard identifying critical security vulnerabilities in LLM applications, serving
  as a benchmark for evaluating security controls in the audit.
Quality_Rating: L
Relevance_Score: H
Fact: The OWASP Top 10 for Large Language Model Applications is a core component of
  the OWASP GenAI Security Project, which is a global, open-source initiative dedicated
  to identifying and mitigating security risks in generative AI. The project has over
  600 contributing experts from more than 18 countries and nearly 8,000 active community
  members. It provides comprehensive guidance for secure development, deployment,
  and governance of generative AI systems. The Top 10 list identifies the most critical
  security vulnerabilities in LLM applications.
Summary: The document is the README for the OWASP Top 10 for Large Language Model
  Applications repository. It explains that the project has evolved into the comprehensive
  OWASP GenAI Security Project, a global initiative to address security and safety
  risks of generative AI. The project's mission is to empower organizations with guidance
  and tools for secure development, deployment, and governance of generative AI systems.
  The OWASP Top 10 for LLM Applications remains a core component, identifying critical
  vulnerabilities. The project has grown from a small group in 2023 to over 600 experts
  from 18 countries and nearly 8,000 community members. The document provides links
  to the project site, mission, contribution guidelines, meeting schedules, and community
  channels like Slack and LinkedIn. It also mentions a newsletter and invites sponsorship
  support.
Section_Context: Regulatory requirements
IIA_Relevance_Explanation: The OWASP Top 10 for LLM Applications is an industry-recognized
  standard identifying critical security vulnerabilities in LLM applications, serving
  as a benchmark for evaluating security controls in the audit.
IIA_Relevance: H
IIA_Confidence: L
Notes: 'Auto-derived categorization: The OWASP Top 10 for LLM Applications is an industry-recognized
  standard identifying critical security vulnerabilities in LLM applications, serving
  as a benc...'
---

# OWASP Top 10 for Large Language Model Applications

## About This Repository

This is the repository for the **OWASP Top 10 for Large Language Model Applications**. However, this project has now grown into the comprehensive **OWASP GenAI Security Project** \- a global initiative that encompasses multiple security initiatives beyond just the Top 10 list.

## OWASP GenAI Security Project

The OWASP GenAI Security Project is a global, open-source initiative dedicated to identifying, mitigating, and documenting security and safety risks associated with generative AI technologies, including large language models (LLMs), agentic AI systems, and AI-driven applications. Our mission is to empower organizations, security professionals, AI practitioners, and policymakers with comprehensive, actionable guidance and tools to ensure the secure development, deployment, and governance of generative AI systems.

**Learn more about our mission and charter:** [Project Mission and Charter](https://genai.owasp.org/project-mission-and-charter/)

**Visit our main project site:** [genai.owasp.org](https://genai.owasp.org/)

## Latest Top 10 for LLM Applications

The OWASP Top 10 for Large Language Model Applications continues to be a core component of our work, identifying the most critical security vulnerabilities in LLM applications.

**Access the latest Top 10 for LLM:** [https://genai.owasp.org/llm-top-10/](https://genai.owasp.org/llm-top-10/)

## Project Background and Growth

The project has evolved significantly since its inception. From a small group of security professionals addressing an urgent security gap in 2023, it has grown into a global community with over 600 contributing experts from more than 18 countries and nearly 8,000 active community members.

**Read our full project background:** [Introduction and Background](https://genai.owasp.org/introduction-genai-security-project/)

## Get Involved

### Contribute to the Project

We welcome all expert ideas, contributions, suggestions, and remarks from security professionals, researchers, developers, and anyone passionate about AI security.

**Learn how to contribute:** [https://genai.owasp.org/contribute/](https://genai.owasp.org/contribute/)

### Join Our Meetings

Participate in our bi-weekly sync meetings and stay connected with the community.

**Meeting information:** [https://genai.owasp.org/meetings/](https://genai.owasp.org/meetings/)

### Connect with the Community

- Join our working group channel on the [OWASP Slack](https://owasp.org/slack/invite) \- sign up and join us on the `#project-top10-for-llm` channel
- [Follow our project LinkedIn page](https://www.linkedin.com/company/owasp-top-10-for-large-language-model-applications/)
- [Subscribe to our newsletter](https://llmtop10.beehiiv.com/subscribe) for periodic updates

## Project Support

We are a not-for-profit, open-source, community-driven project. If you are interested in supporting the project with resources or becoming a sponsor to help us sustain community efforts and offset operational and outreach costs, visit the [Sponsor Section](https://genai.owasp.org/sponsorship) on our website.

**Thank you to our current [Sponsors and Supporters](https://genai.owasp.org/supporters/)**

## Educational Resources

New to LLM Application security? Check out our [resources page](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/wiki/Educational-Resources) to learn more.

* * *

# OWASP Top 10 for Large Language Model Applications version 1.1

## LLM01: Prompt Injection

Manipulating LLMs via crafted inputs can lead to unauthorized access, data breaches, and compromised decision-making.

## LLM02: Insecure Output Handling

Neglecting to validate LLM outputs may lead to downstream security exploits, including code execution that compromises systems and exposes data.

## LLM03: Training Data Poisoning

Tampered training data can impair LLM models leading to responses that may compromise security, accuracy, or ethical behavior.

## LLM04: Model Denial of Service

Overloading LLMs with resource-heavy operations can cause service disruptions and increased costs.

## LLM05: Supply Chain Vulnerabilities

Depending upon compromised components, services or datasets undermine system integrity, causing data breaches and system failures.

## LLM06: Sensitive Information Disclosure

Failure to protect against disclosure of sensitive information in LLM outputs can result in legal consequences or a loss of competitive advantage.

## LLM07: Insecure Plugin Design

LLM plugins processing untrusted inputs and having insufficient access control risk severe exploits like remote code execution.

## LLM08: Excessive Agency

Granting LLMs unchecked autonomy to take action can lead to unintended consequences, jeopardizing reliability, privacy, and trust.

## LLM09: Overreliance

Failing to critically assess LLM outputs can lead to compromised decision making, security vulnerabilities, and legal liabilities.

## LLM10: Model Theft

Unauthorized access to proprietary large language models risks theft, competitive advantage, and dissemination of sensitive information.

* * *

[Edit on GitHub](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/master/index.md)