# CyberSecurity Projects

A week-by-week portfolio for the Maxim Nyansa cybersecurity bootcamp in Ghana, **5 October–25 December 2026**. The work is arranged for a beginner who wants blue-team practice: detection, logs, and careful reporting. The home lab is planned for a laptop with **32 GB of RAM** and VirtualBox.

This page is a template. It does not invent a biography.

- **Name:** [Your name]
- **Location:** [City, if you want to publish it]
- **Email:** [you@example.com]
- **LinkedIn:** [https://www.linkedin.com/in/your-profile]
- **GitHub:** [https://github.com/your-handle]

## How to use this repository

Each week has its own folder. Each deliverable has a folder inside that week, with a README that states the goal, what is already here, how to run or repeat it, and prompts for what you learned. Fill those prompts yourself. Where a result depends on your virtual machine, the file says so and leaves the evidence blank.

Sample logs, sample control sheets, and example risk rows are marked synthetic or `example=yes`. They are teaching data. They are not findings from a real network.

Labs stay on systems you are allowed to test. The home lab uses a VirtualBox host-only network. Week 10 adds an assessment VM only behind a written scope. This repository does not include exploit procedures, malware samples, or offensive automation.

## Skills this portfolio is built to show

| Area | Where it lives |
| --- | --- |
| CIA, risk language, ethics, and Ghana law study notes (Act 1038, Act 843, Act 772, Bank of Ghana CISD) | Week 1 |
| TCP/IP, addressing, and a lab network plan | Week 2 |
| Operating systems, a workstation baseline, read-only hardening checks, backups, Wazuh and a Windows endpoint plan | Week 3 |
| Risk scoring, an ISO 27001 study checklist, a practice audit, and a tabletop | Week 4 |
| Secure development, input handling, XSS prevention, configuration review | Week 5 |
| Databases, permissions, recovery, and parameterised queries | Week 6 |
| Hashing, password hashing, symmetric encryption, certificates, TLS and IPsec | Week 7 |
| Passwords, MFA, journeys, RBAC and ABAC, least privilege | Week 8 |
| Cloud models, shared responsibility, a cloud checklist and risk register | Week 9 |
| Authorised assessment reporting, defensive phishing and malware notes, Kali added to the lab | Week 10 |
| Compliance counts, log triage, Sigma rules mapped to MITRE ATT&CK, a local threat-intel summary | Week 11 |
| Incident notes and report, a 40-question revision quiz, capstone outline, next steps | Week 12 |

The ISO checklist is study material. It is not a certification. The law notes are not legal advice. Read the official Act or directive before you quote a section.

## Roadmap

| Week | Dates | Folder | Projects |
| --- | --- | --- | --- |
| 1 Foundations | 5–9 Oct 2026 | [week-01-foundations](week-01-foundations/) | [Learning plan](week-01-foundations/personal-learning-plan/), [team charter](week-01-foundations/team-project-charter/), [risk register](week-01-foundations/risk-register/), [ethics and Ghana law](week-01-foundations/ethics-case-studies/), [careers map](week-01-foundations/careers-map/) |
| 2 TCP/IP | 12–16 Oct 2026 | [week-02-tcp-ip-networking](week-02-tcp-ip-networking/) | [Network map](week-02-tcp-ip-networking/network-map/), [protocol reference](week-02-tcp-ip-networking/protocol-reference/), [addressing practice](week-02-tcp-ip-networking/addressing-practice/), [home-lab network](week-02-tcp-ip-networking/home-soc-lab-network/) |
| 3 Systems and hardening | 19–23 Oct 2026 | [week-03-systems-and-hardening](week-03-systems-and-hardening/) | [Architecture notes](week-03-systems-and-hardening/system-architecture-notes/), [workstation baseline](week-03-systems-and-hardening/workstation-baseline/), [hardening audit](week-03-systems-and-hardening/hardening-audit/), [backups and logging](week-03-systems-and-hardening/backup-and-logging/), [hardening report](week-03-systems-and-hardening/system-hardening-report/), [Wazuh server](week-03-systems-and-hardening/home-soc-lab-wazuh/), [Windows endpoint](week-03-systems-and-hardening/home-soc-lab-windows-endpoint/) |
| 4 Security management | 26–30 Oct 2026 | [week-04-security-management](week-04-security-management/) | [Risk sprint](week-04-security-management/risk-assessment-sprint/), [ISO 27001 gap check](week-04-security-management/iso-27001-gap-check/), [role-play audit](week-04-security-management/role-play-audit/), [tabletop](week-04-security-management/tabletop-crisis-simulation/) |
| 5 Application security | 2–6 Nov 2026 | [week-05-application-security](week-05-application-security/) | [SDLC checklist](week-05-application-security/secure-development-checklist/), [input validation](week-05-application-security/input-validation/), [XSS awareness](week-05-application-security/xss-awareness/), [insecure configuration](week-05-application-security/insecure-configuration/), [secure code review](week-05-application-security/secure-code-review/) |
| 6 Databases | 9–13 Nov 2026 | [week-06-database-security](week-06-database-security/) | [Models](week-06-database-security/database-models/), [integrity](week-06-database-security/data-integrity/), [roles and recovery](week-06-database-security/role-permission-matrix/), [security checklist](week-06-database-security/database-security-checklist/) |
| 7 Cryptography | 16–20 Nov 2026 | [week-07-cryptography](week-07-cryptography/) | [Encryption and hashing](week-07-cryptography/encryption-hashing-practice/), [key policy](week-07-cryptography/key-management-policy/), [certificate inspection](week-07-cryptography/certificate-inspection/), [TLS and IPsec](week-07-cryptography/secure-communications/) |
| 8 Identity and access | 23–27 Nov 2026 | [week-08-identity-access-management](week-08-identity-access-management/) | [Password and MFA policy](week-08-identity-access-management/password-mfa-policy/), [user journey](week-08-identity-access-management/iam-user-journey/), [access matrix](week-08-identity-access-management/access-control-matrix/), [least privilege](week-08-identity-access-management/least-privilege-proposal/) |
| 9 Cloud | 30 Nov–4 Dec 2026 | [week-09-cloud-security](week-09-cloud-security/) | [Deployment comparison](week-09-cloud-security/cloud-deployment-comparison/), [shared responsibility](week-09-cloud-security/shared-responsibility/), [cloud checklist](week-09-cloud-security/cloud-security-checklist/), [cloud risk register](week-09-cloud-security/cloud-risk-register/) |
| 10 Authorised assessment | 7–11 Dec 2026 | [week-10-vulnerability-assessment](week-10-vulnerability-assessment/) | [Scope](week-10-vulnerability-assessment/assessment-scope/), [phishing awareness](week-10-vulnerability-assessment/phishing-awareness/), [malware defence](week-10-vulnerability-assessment/malware-defence/), [assessment report](week-10-vulnerability-assessment/vulnerability-assessment-report/), [remediation](week-10-vulnerability-assessment/remediation-recommendations/), [Kali lab](week-10-vulnerability-assessment/home-soc-lab-kali/) |
| 11 Automation for defence | 14–18 Dec 2026 | [week-11-ai-soc-automation](week-11-ai-soc-automation/) | [Compliance counts](week-11-ai-soc-automation/compliance-automation/), [log triage](week-11-ai-soc-automation/soc-alert-triage/), [Sigma rules](week-11-ai-soc-automation/sigma-rules/), [threat-intel summary](week-11-ai-soc-automation/threat-intel-summary/), [authorised-test review](week-11-ai-soc-automation/authorised-test-review/) |
| 12 Incident response and capstone | 21–25 Dec 2026 | [week-12-incident-response-capstone](week-12-incident-response-capstone/) | [Response notes](week-12-incident-response-capstone/incident-response-notes/), [incident report](week-12-incident-response-capstone/incident-report/), [mock assessment](week-12-incident-response-capstone/mock-assessment/), [capstone outline](week-12-incident-response-capstone/capstone-outline/), [next steps](week-12-incident-response-capstone/next-step-plan/) |

## Home SOC lab

The lab is threaded through the weeks instead of being one isolated folder.

| Piece | When | Folder |
| --- | --- | --- |
| Host-only network, `192.168.56.0/24`, RAM plan | Week 2 | [home-soc-lab-network](week-02-tcp-ip-networking/home-soc-lab-network/) |
| Wazuh on Ubuntu Server at `192.168.56.10` | Week 3 | [home-soc-lab-wazuh](week-03-systems-and-hardening/home-soc-lab-wazuh/) |
| Windows VM, Sysmon, Wazuh agent at `192.168.56.20` | Week 3 | [home-soc-lab-windows-endpoint](week-03-systems-and-hardening/home-soc-lab-windows-endpoint/) |
| Kali at `192.168.56.30`, after a signed scope | Week 10 | [home-soc-lab-kali](week-10-vulnerability-assessment/home-soc-lab-kali/) |
| Log triage and Sigma rules for brute force (T1110) and new admins (T1098) | Week 11 | [soc-alert-triage](week-11-ai-soc-automation/soc-alert-triage/), [sigma-rules](week-11-ai-soc-automation/sigma-rules/) |

Do not run all three guests at full size if the laptop starts swapping. The Wazuh VM is the one that needs the memory. Nothing in this repository is a screenshot of that lab. Those files are yours to add under a project's `evidence/` folder when you have them.

## Run the tests

Python 3.11 or newer is enough. The exercises use the standard library plus `pytest`, `cryptography`, and `PyYAML`.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

You should see passing tests for addressing, the read-only audit, safe input handling, parameterised database access, hashing and encryption, certificate inspection, the password policy, compliance counts, log triage, Sigma checks, the threat-intel summary, and the mock-exam scorer.

Private keys are ignored by `.gitignore` (`*.key`, `*.p12`, `*.pfx`). Do not commit passwords, agent enrolment tokens, or logs that contain personal data.

## What you still fill in

- Your name and links on this page, in the learning plan, and in the careers map
- Every project's "What I learned" prompts and evidence lines
- Risk scores, audit results, and checklist statuses, only after you have done the work
- Virtual-machine output: Wazuh version, agent id, hardening-audit text, restore tests
- The Week 10 scope signatures, findings, and remediation rows
- Your mock answers, after you try the questions
- The capstone slides and the next-step plan

## Licence

The existing [MIT Licence](LICENSE) applies to this repository.
