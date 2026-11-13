# Trainee lab guides

Twelve hands-on labs for James Ackah Blay. Each PDF is the guide to follow. The tutor answer key sits beside it as `TUTOR-ANSWER-KEY.md` and is not inside the PDF.

Regenerate the PDFs from the Markdown sources:

```bash
sudo apt-get install pandoc weasyprint
python3 labs/build_pdfs.py
```

| Week | Guide | Time | Difficulty |
| --- | --- | --- | --- |
| 1 | [Lab 01 PDF](../week-01-foundations/lab-01-risk-register-and-cia/LAB-01-risk-register-and-cia.pdf) | 3 h | Foundation |
| 2 | [Lab 02 PDF](../week-02-tcp-ip-networking/lab-02-network-and-packet-flow/LAB-02-network-and-packet-flow.pdf) | 4 h | Foundation |
| 3 | [Lab 03 PDF](../week-03-systems-and-hardening/lab-03-hardening-and-wazuh/LAB-03-hardening-and-wazuh.pdf) | 6 h | Intermediate |
| 4 | [Lab 04 PDF](../week-04-security-management/lab-04-iso-gap-and-tabletop/LAB-04-iso-gap-and-tabletop.pdf) | 4 h | Intermediate |
| 5 | [Lab 05 PDF](../week-05-application-security/lab-05-web-logs-and-appsec/LAB-05-web-logs-and-appsec.pdf) | 5 h | Intermediate |
| 6 | [Lab 06 PDF](../week-06-database-security/lab-06-database-security/LAB-06-database-security.pdf) | 5 h | Intermediate |
| 7 | [Lab 07 PDF](../week-07-cryptography/lab-07-openssl-pki-tls/LAB-07-openssl-pki-tls.pdf) | 4 h | Intermediate |
| 8 | [Lab 08 PDF](../week-08-identity-access-management/lab-08-iam-and-account-abuse/LAB-08-iam-and-account-abuse.pdf) | 6 h | Advanced |
| 9 | [Lab 09 PDF](../week-09-cloud-security/lab-09-cloud-iam-and-logging/LAB-09-cloud-iam-and-logging.pdf) | 5 h | Advanced |
| 10 | [Lab 10 PDF](../week-10-vulnerability-assessment/lab-10-authorised-assessment/LAB-10-authorised-assessment.pdf) | 6 h | Advanced |
| 11 | [Lab 11 PDF](../week-11-ai-soc-automation/lab-11-soc-automation/LAB-11-soc-automation.pdf) | 6 h | Advanced |
| 12 | [Lab 12 PDF](../week-12-incident-response-capstone/lab-12-incident-response-capstone/LAB-12-incident-response-capstone.pdf) | 8 h | Capstone |

Governance labs (1, 4, 9, and the compliance half of 11) use the [GRC Lab](https://grclab.purplecop.io/lab). Save your own exports. The guides do not describe that site and do not invent your results.

## Skills these labs are built to practise

This is a practice map, not a claim of three years on a shift. The hours above are the lab time, not time served.

| Skill a SOC or blue-team role uses | Labs |
| --- | --- |
| CIA, risk statements, and legal limits | 1 |
| Subnetting, packet flow, and a contained lab network | 2 |
| Hardening, backups, Sysmon, and a SIEM agent | 3 |
| Control gaps, audit notes, and a tabletop | 4 |
| Web log review and safe output handling | 5 |
| Database roles, statement logs, and restores | 6 |
| Hashing, a local CA, and certificate fields | 7 |
| Passwords, MFA gaps, RBAC, and admin-change detection | 8 |
| Shared responsibility, IAM, and cloud logs, with a cost cap | 9 |
| Scoped assessment, narrow discovery, and a report | 10 |
| Alert summaries, Sigma, ATT&CK, and human review | 11 |
| Containment, preservation, recovery, and a capstone write-up | 12 |

## What you install

The repository tests need Python 3.11+ and `requirements.txt`. The labs themselves also expect, when you reach them:

- VirtualBox, an Ubuntu Server VM, and a Windows VM (Weeks 2–3). Kali only in Week 10, host-only.
- `tcpdump` and Wireshark (Week 2).
- Wazuh from the current official quickstart, plus Sysmon from Microsoft (Week 3).
- Docker, if you choose the local Juice Shop or Keycloak options (Weeks 5 and 8). Both are bound to `127.0.0.1`.
- PostgreSQL (Week 6) and OpenSSL (Week 7).
- AWS CLI only if you open an account, after a 1 USD budget alarm (Week 9).
- `nmap` (Week 10). Greenbone is optional and follows its own current install guide.
- Pandoc and WeasyPrint only if you want to rebuild the PDFs.
