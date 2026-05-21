---
Document_File_Name: aws_genai_security_scoping_matrix.md
IIA_Type: UNK
Quality_Rating: L
Relevance_Score: L
Fact: We use essential cookies and similar tools that are necessary to provide our
  site and services. We use performance cookies to collect anonymous statistics, so
  we can understand how customers use our site and make improvements.
Summary: 'Document_File_Name: aws_genai_security_scoping_matrix.md. IIA_Type: UNK.
  Quality_Rating: L. Relevance_Score: L. Fact: We use essential cookies and similar
  tools that are necessary to provide our. site and services. We use performance cookies
  to collect anonymous statistics, so. we can understand how customers use our site
  and make improvements. Quality_Rating: L. Relevance_Score: L.'
Section_Context: Document overview
IIA_Relevance_Explanation: Listed to preserve coverage; manual review required to
  extract planning evidence.
IIA_Relevance: L
IIA_Confidence: L
Notes: Auto-derived from scan; verify content during manual review.
---

## Select your cookie preferences

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

AcceptDeclineCustomize

## Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

### Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

### Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

### Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

### Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

CancelSave preferences

## Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our [Cookie Notice](https://aws.amazon.com/legal/cookies/).

Allow cross-context behavioral adsOpt out of cross-context behavioral ads

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form [here](https://pulse.aws/application/ZRPLWLL6?p=0).

For more information about how AWS handles your information, read the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

CancelSave preferences

## Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Dismiss

 [Skip to main content](https://aws.amazon.com/ai/security/generative-ai-scoping-matrix/#aws-page-content-main)

AI

- [Overview](https://aws.amazon.com/ai/)
- More


- [AI](https://aws.amazon.com/ai/)
- [Security](https://aws.amazon.com/ai/security/)
- AI Security Scoping Matrix

# AI Security Scoping Matrix

## Overview

As organizations increasingly adopt generative AI technologies, understanding the security implications becomes critical. Core security disciplines, like identity and access management, data protection, privacy and compliance, application security, and threat modeling are still critically important for generative AI workloads, just as they are for any other workload. But beyond emphasizing long-standing security practices, it’s crucial to understand the unique risks and additional security considerations that generative AI workloads bring.

The **AI Security Scoping Matrix** is a comprehensive framework designed to help organizations assess and implement security controls throughout the AI lifecycle. It breaks down security considerations into specific categories, enabling a focused approach to securing AI applications.


Play

[image omitted]

[image omitted]

Video Player is loading.

Play Video

PlaySkip BackwardSkip Forward

Mute

Current Time 0:00

/

Duration 0:00

Loaded: 0%

Stream Type LIVE

Seek to live, currently behind liveLIVE

Remaining Time -0:00

1x

Playback Rate

Chapters

- Chapters

Descriptions

- descriptions off, selected

Captions

- captions and subtitles off, selected

Audio Track

Picture-in-PictureFullscreen

This is a modal window.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

ResetDone

Close Modal Dialog

End of dialog window.

## AI Security Scoping Matrix

A mental model to classify use cases

100%

## Determining your scope

The first step is to determine which scope your use case fits into. The scopes are numbered 1–5, representing least ownership to greatest ownership your organization has over the AI model and its associated data.

### Scope 1: Consumer app

Your organization consumes a public third-party generative AI service, either at no-cost or paid. These are often “consumer grade” applications and may not be made for enterprise or commercial use. At this scope you don’t own or see the training data or the model, and you cannot modify or augment it. You invoke APIs or directly use the application according to the terms of service of the provider.

**Example:** An employee interacts with a generative AI chat application via a public website to generate ideas for an upcoming marketing campaign.


### Scope 2: Enterprise app

Your organization uses a third-party enterprise application that has generative AI features embedded within, and a business relationship is established between your organization and the vendor. Scope 2 applications often have terms and conditions that are aimed at enterprise customers, designed to offer additional protections.

**Example:** You use a third-party enterprise scheduling application that has a generative AI capability embedded within to help draft meeting agendas.


### Scope 3: Pre-trained models

Your organization builds its own application using an existing third-party generative AI foundation model. You directly integrate it with your workload through an application programming interface (API).

**Example:** You build a customer support chatbot that integrates your own data using Retrieval-Augmented Generation (RAG) and uses a foundation model through a managed AI platform.


### Scope 4: Fine-tuned models

Your organization refines an existing third-party generative AI foundation model by fine-tuning it with data specific to your business, generating a new, enhanced model that’s specialized to your workload.

**Example:** You require a model with in-depth medical domain expertise to summarize patient records in an Electronic Health Record (EHR) system. Fine-tuning can be used to align the system's output to match the style expected by doctors and provide the system training on domain specific terminology.


### Scope 5: Self-trained models

Your organization builds and trains a generative AI model from scratch using data that you own or acquire. You own every aspect of the model.

**Example:** Your organization aims to create a model for generating high-quality video content, such as building a custom solution for super slow-motion video interpolation. By training a model on specialized video data, you can license this advanced video creation technology to companies in the media and entertainment industry.


## What to prioritize

Your workload is scoped and now you need to enable your business to move forward fast, yet securely. In the Generative AI Security Scoping Matrix, we identify five security disciplines that span the different types of generative AI solutions.

- Governance and compliance – The policies, procedures, and reporting needed to empower the business while minimizing risk.
- Legal and privacy – The specific regulatory, legal, and privacy requirements for using or creating generative AI solutions.
- Risk management – Identification of potential threats to generative AI solutions and recommended mitigations.
- Controls – The implementation of security controls that are used to mitigate risk.
- Resilience – How to architect generative AI solutions to maintain availability and meet business SLAs.

Let’s explore a few examples of opportunities you should prioritize.

## Security Considerations Across Scopes

- Governance and compliance
- Legal and privacy
- Risk management
- Controls
- Resilience

### Governance and compliance

When managing Scopes 1 and 2, it's crucial to comply with terms of service, licensing agreements, and data sovereignty requirements. For Scope 1 applications, prioritize the use of public, non-proprietary data, as service providers may use submitted data to enhance their models or services. Scope 2 applications should be developed with robust controls, contractual protections, and opt-out options to safeguard your organization’s proprietary and sensitive data, ensuring it is not utilized for model training or improvement. These applications are typically tailored for enterprise use cases.

For tasks that may be unique to your organization or customer needs, like summarizing proprietary or sensitive business data, generating unique insights, or automating internal processes, you may need to build your own application from Scopes 3 to 5. These scopes allow for the use of your data in training, fine-tuning, or as model output. For instance, even though you aren’t fine-tuning or training your data in to Scope 3 LLMs, you can still use [Retrieval Augmented Generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/), [Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/), and [Agents](https://aws.amazon.com/bedrock/agents/) for enhancing model responses and contextual actions without fine-tuning the model.

In Scopes 4 and 5, train your model on domain-specific data, avoiding sensitive data such as PII. Ensure that the resulting model is classified at the highest level of data sensitivity used during training. Access to run inference on the model should be restricted to users authorized for that classification level. For data like PII or frequently changing transactional data, consider adding it back in during inference using Retrieval-Augmented Generation (RAG) or agent-based workflows, rather than incorporating it into the model itself.


### Legal and privacy

From a legal perspective, it’s important to understand both the service provider’s end-user license agreement (EULA), terms of services (TOS), and any other contractual agreements necessary to use their service across Scopes 1 through 4. For Scope 5, your legal teams should provide their own contractual terms of service for any external use of your models. Also, for Scope 3 and Scope 4, be sure to validate both the service provider’s legal terms for the use of their service, as well as the model provider’s legal terms for the use of their model within that service.

Additionally, consider the privacy concerns if the [European Union’s General Data Protection Regulation (GDPR)](https://aws.amazon.com/compliance/gdpr-center/) “right to erasure” or “right to be forgotten” requirements are applicable to your business. Carefully consider the impact of training or fine-tuning your models with data that you might need to delete upon request. The only fully effective way to remove data from a model is to delete the data from the training set and train a new version of the model. This isn’t practical when the data deletion is a fraction of the total training data and can be very costly depending on the size of your model.


### Risk management

While AI-enabled applications resemble traditional ones, their interactive nature with large language models (LLMs) demands extra vigilance and specific guardrails. It's crucial to identify risks associated with generative AI workloads and start mitigating them.

Risk identification can generally be done through risk assessments and threat modeling. For Scopes 1 and 2, evaluate the risks stemming from third-party providers and understand their risk mitigation strategies. You must also recognize your own risk management responsibilities as a service consumer.

For Scopes 3, 4, and 5, implement threat modeling that addresses both AI safety and data security risks, with a focus on unique LLM threats like prompt injection. This involves crafting inputs that can manipulate LLM responses, potentially leading to data breaches or unauthorized access. Recent guidance from [NIST](https://www.nist.gov/itl/ai-risk-management-framework), [MITRE](https://atlas.mitre.org/), and [OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/) identifies prompt injection as a primary threat, comparable to traditional injection attacks like SQL. Mitigate this risk by applying fine-grained authorization and data filtering before it reaches the LLM, and use Bedrock Guardrails for additional protection.

Emerging threats in generative AI require adapting traditional cybersecurity measures and collaborating closely with development teams to effectively model threats and establish tailored best practices.


### Controls

Implementing robust controls is crucial for enforcing compliance, policy, and security requirements, thereby mitigating risks associated with generative AI workloads. One of the key considerations is managing identity and access to your models. Unlike traditional databases that offer fine-grained security controls, foundation models have no concept of access control to data stored within the model or data provided at inference time. This makes it essential to implement least privilege access control to data before it’s added as context into the inference request.


To achieve this, you can leverage application layers that interact with the model through endpoints like Amazon Bedrock. These layers should incorporate identity solutions such as Amazon Cognito or AWS IAM Identity Center to authenticate and authorize users. By tailoring access based on roles, attributes, and user communities, you can limit specific actions and help ensure that sensitive data is protected.

Additionally, as your AI workloads evolve, it’s important to continually assess and update your controls to adapt to new threats and changes in data sensitivity. Incorporating advanced techniques such as Retrieval-Augmented Generation (RAG) can allow you to provide real-time data without compromising the integrity of the model. These strategies, combined with ongoing threat modeling, help to maintain a secure and compliant environment for your generative AI applications.


### Resilience

Availability is a key component of security as called out in the [C.I.A. triad](https://csrc.nist.gov/glossary/term/cia). Building resilient applications is critical to meeting your organization’s availability and business continuity requirements. For Scope 1 and 2, you should understand how the provider’s availability aligns to your organization’s needs and expectations. Carefully consider how disruptions might impact your business should the underlying model, API, or presentation layer become unavailable. Additionally, consider how complex prompts and completions might impact usage quotas, or what billing impacts the application might have.


For Scopes 3, 4, and 5, make sure that you set appropriate timeouts to account for complex prompts and completions. You might also want to look at prompt input size for allocated character limits defined by your model. Also consider existing best practices for resilient designs such as [backoff and retries](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html) and [circuit breaker patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html) to achieve the desired user experience. When using vector databases, having a high availability configuration and disaster recovery plan is recommended to be resilient against different failure modes.


Instance flexibility for both inference and training model pipelines are important architectural considerations in addition to potentially reserving or pre-provisioning compute for highly critical workloads. When using managed services like Amazon Bedrock or SageMaker, you must validate AWS Region availability and feature parity when implementing a multi-Region deployment strategy. Similarly, for multi-Region support of Scope 4 and 5 workloads, you must account for the availability of your fine-tuning or training data across Regions. If you use SageMaker to train a model in Scope 5, use [checkpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints.html) to save progress as you train your model. This will allow you to resume training from the last saved checkpoint if necessary.


Be sure to review and implement existing application resilience best practices established in the [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/) and within the [Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) and [Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) of the Well Architected Framework.


## AWS resources on Generative AI and security best practices

[Use Case **Generative AI Use Cases at AWS**\\
\\
View use cases](https://aws.amazon.com/ai/generative-ai/use-cases/)

[Blog **A secure approach to generative AI with AWS**\\
\\
Read the blog](https://aws.amazon.com/blogs/machine-learning/a-secure-approach-to-generative-ai-with-aws/)

[FAQs **What is Generative AI?**\\
\\
Learn more](https://aws.amazon.com/what-is/generative-ai/)

[Blog **Top 10 Security Improvements for Your AWS account**\\
\\
Read the blog](https://aws.amazon.com/blogs/security/top-10-security-items-to-improve-in-your-aws-account/)

[Documentation **AWS Well-Architected Security Pillar documentation**\\
\\
View the document](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)

[Documentation **AWS Machine Learning Lens - Well-Architected Framework**\\
\\
View the document](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html)

## Get started with Generative AI Security Scoping Matrix

[Blog\\
\\
**Introduction to the Generative AI Security Scoping Matrix**\\
\\
Read the blog](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/)

[Blog\\
\\
**Securing generative AI: Applying relevant security controls**\\
\\
Read the blog](https://aws.amazon.com/blogs/security/securing-generative-ai-applying-relevant-security-controls/)
