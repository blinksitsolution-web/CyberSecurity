# Artificial Intelligence Use, Governance and Security Policy

Policy document prepared by James Ackah-Blay as coursework. Version 1.0, 37 pages, classification Internal, status Submission-Ready. Effective date 10 October 2026. Next review date 10 October 2027. Review frequency at least annually.

The document's own control table lists the owner as Compliance / Information Security and the change-history author as Compliance / InfoSec. It does not put his name on the cover. It is filed under Week 11 because that week is AI and cybersecurity automation, including AI for governance and compliance (14–18 December 2026). He wrote the policy in October, before that class. The week's automation exercises are not started.

Full document: [ai-use-governance-and-security-policy.pdf](ai-use-governance-and-security-policy.pdf)

## Context

An enterprise-style policy for secure, responsible, and compliant use of AI, including generative AI. The organisation is not named. Scope covers employees, management, interns, contractors, third parties, organisational systems, and AI that is built, bought, or used, including public, commercial, open-source, and internal tools, on organisational or personal devices.

Status is Submission-Ready. This page does not describe it as an approved policy of an employer.

## Role

Author of the submitted policy. Inside the document, ownership sits with Compliance / Information Security, and an approval table lists role holders. Those names are left in the PDF and are not repeated here.

## Frameworks and methods

Section 33 says the policy should be aligned, where applicable, with:

- ISO/IEC 27001:2022 — Information Security Management Systems
- ISO/IEC 27002:2022 — Information Security Controls
- ISO/IEC 42001:2023 — Artificial Intelligence Management Systems
- ISO/IEC 23894 — Artificial Intelligence Risk Management
- NIST AI Risk Management Framework
- NIST Cybersecurity Framework
- Applicable data protection, cybersecurity, intellectual property, employment, and other legal requirements

The scoring method in section 35.5 is likelihood 1–5 times impact 1–5. Bands: 1–4 Low, 5–9 Moderate, 10–16 High, 17–25 Critical. The policy says those ratings are illustrative starting estimates, not measured incident frequencies.

## Deliverables and findings

The policy has 36 numbered sections plus operational appendices A–G:

- Appendix A — AI risk assessment matrix
- Appendix B — AI tool approval form
- Appendix C — acceptable and prohibited use matrix
- Appendix D — AI system inventory template
- Appendix E — AI incident reporting template
- Appendix F — AI exception request form
- Appendix G — AI governance control checklist

Governance design he wrote down:

- An AI Oversight Committee chaired by an executive sponsor, meeting at least quarterly and after a serious incident.
- Eight lifecycle stages before and after deployment: proposal and classification, security/privacy and impact assessment, design and data approval, independent testing, authorization, controlled deployment, monitoring and periodic review, and retirement or replacement. No production deployment bypasses the approval gate.
- Minimum review: critical and high-risk systems at least quarterly, moderate-risk at least every six months, low-risk annually.

Appendix A is a worked matrix labelled as the assessment to complete before an AI system with more than minimal risk is introduced. Two of the illustrative rows:

| Risk area | Likelihood | Impact | Score | Existing control named in the row |
| --- | --- | --- | --- | --- |
| Information security — unauthorised disclosure | 3 | 4 | 12 | DLP filters, prompt rules |
| Privacy — exposure of personal data | 2 | 4 | 8 | DPA, privacy guidelines |

A score of 12 sits in the policy's High band (10–16). A score of 8 sits in Moderate (5–9). The same appendix states the figures are the matrix to use; section 35.5 says the starting estimates are not measured frequencies.

Security testing listed in section 35.4 includes prompt injection, jailbreaks, malicious files, data exfiltration, insecure output handling, model poisoning, model theft, excessive agency, exposed API keys, and insecure third-party plugins. The policy requires a human approval step before an AI workflow sends messages, transfers money, changes records, executes code, or accesses sensitive services.

## Skills demonstrated

Drafting an AI governance and security policy, mapping it to ISO/IEC 27001, 27002, 42001, and 23894 and to the NIST AI RMF and NIST Cybersecurity Framework, and writing a 5×5 AI risk matrix with owners and treatments. The scores are policy illustrations. This is not a claim of security operations, incident response, or IAM work in a live environment.
