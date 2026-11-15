# Project 4 — IT system risk assessment (individual)

Yes You Can Cyber Secure course project, prepared by James Ackah-Blay. Assessment date 2 November 2026. Next review stated as February 2027. 58 pages. The course runs February–December 2026 and is in progress. This project is one submitted assignment, not a completed certification.

Full document: [project-4-exchange-and-cisco-asa-risk-assessment.pdf](project-4-exchange-and-cisco-asa-risk-assessment.pdf)

## Context

Trinity Valley Health Partners (TVHP) is a fictional organisation. The report defines it as a regional healthcare provider in Dallas, Texas, with about 1,400 staff and 9 clinics, treated as a HIPAA covered entity that handles electronic protected health information. Every existing control is an assumed as-is state, not an observed fact. System details are scenario assumptions: Exchange Server 2019 CU15 as a two-node database availability group on Windows Server 2022 with about 1,400 mailboxes, and an active/standby pair of Cisco ASA 5516-X firewalls on ASA 9.16.x serving about 600 remote staff and two support vendors.

## Role

Individual. The report's team table lists one assessor: James Ackah-Blay, GRC analyst / risk assessor, responsible for scoping, risk identification and analysis, rating, mitigation design, GRC Practice Lab entry, the risk register, and the report. Risk owners in the register are job roles in the fictional organisation, not named people.

## Frameworks and methods

- NIST SP 800-30 Rev. 1 for the Tier 3 risk assessment, including threat-source and threat-event tables and the qualitative levels in Table I-2.
- Risk score = likelihood (1–5) × impact (1–5), range 1–25.
- GRC Practice Lab as the tool used to record assets, risks, the heatmap, and controls.
- Control references in the register to NIST SP 800-53, CIS Controls, NIST CSF 2.0, and the HIPAA Security Rule. The ASA objectives also evaluate assumed controls against CIS Controls v8, NIST CSF 2.0, HIPAA, and the PCI DSS v4.0.1 rule-review requirement.
- CISA Known Exploited Vulnerabilities catalog entries and CISA directives cited for Exchange and ASA issues.

Lab band legend printed with the heatmap: Critical 20–25, High 12–19, Medium 6–11, Low 1–5.

## Deliverables and findings

Two system assessments and one combined register of 20 open risks.

**Microsoft Exchange Server 2019 (EXCH01/EXCH02), assessed 2 November 2026.** Ten risks: 2 Critical and 8 High on the lab scale. No risk was rated below High. Overall inherent risk: Critical (NIST SP 800-30: Very High). NIST qualitative split printed in the summary: Very High 2, High 5, Moderate 3.

Highest Exchange risks:

| ID | Score | Lab band | Subject |
| --- | --- | --- | --- |
| EX-01 | 20 (Likely 4 × Severe 5) | Critical | Unsupported Exchange 2019 after extended support ended 14 October 2025 and the paid Extended Security Update programme ended 31 October 2026 |
| EX-02 | 20 (4 × 5) | Critical | Internet-published Exchange web endpoints, with ProxyLogon, ProxyShell, and ProxyNotShell cited from the CISA KEV catalog |
| EX-05 | 16 (4 × 4) | High | Password-only OWA and ActiveSync |

The recommended direction is migration to Exchange Server Subscription Edition or Exchange Online by 31 March 2027. Target residual after the recommended controls: 7 Medium and 3 Low, with no High or Critical remaining. Those residual figures are planned.

**Cisco ASA 5516-X and Secure Client remote-access VPN (DAL-FW01/02), same date.** Ten risks: 3 Critical, 5 High, and 2 Medium. Overall inherent risk: Critical (NIST SP 800-30: Very High). NIST qualitative split: Very High 3, High 4, Moderate 2, Low 1.

Highest ASA risks:

| ID | Score | Lab band | Subject |
| --- | --- | --- | --- |
| ASA-03 | 25 (Almost Certain 5 × Severe 5) | Critical | Password-only VPN logins (CVE-2023-20269). The report cites CISA advisory AA24-109A |
| ASA-01 | 20 | Critical | ASA 5516-X past Cisco's Last Date of Support on 31 August 2026, unable to run ASA 9.17 or later |
| ASA-02 | 20 | Critical | VPN web-server remote code execution CVE-2025-20333 and CVE-2025-20362, tied to CISA Emergency Directive 25-03 |

Dated actions in the ASA summary: verify the build and complete the Emergency Directive 25-03 hunt by 15 November 2026, enforce MFA on every VPN profile by 30 November 2026, remove management access from the outside interface by 15 December 2026, and replace the hardware by 31 March 2027. Target residual: 6 Medium and 4 Low.

**Lab evidence captured 2 November 2026.** The heatmap caption records 20 total risks, 5 Critical and 13 High. It also states that no treatments were recorded in the lab yet (0/20 treated), so the lab residual heatmap equals the inherent heatmap. The control-library caption says 11 controls were recorded so far. Residual ratings in the written register are planned values, not lab entries.

## Skills demonstrated

Individual Tier 3 risk assessment under NIST SP 800-30: asset scoping, threat and vulnerability statements, 5×5 scoring, a 20-row register with owners and target dates, and control references to NIST SP 800-53, CIS Controls, NIST CSF 2.0, and HIPAA. The scenario, the control baseline, and the residual scores are training assumptions for a fictional healthcare provider.
