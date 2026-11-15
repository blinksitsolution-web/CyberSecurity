# Project 5 — Group 4 GRC virtual lab

**Team project.** James Ackah-Blay contributed as a member of Group 4. The report is written as "we". It does not name individual authors or divide sections by person, so this page does not assign findings to him alone and does not list classmates.

File date: 30 October 2026, the Friday of Week 4 (security management, risk and governance, 26–30 October 2026). The report does not name the training provider. It is filed here because the subject matches that week.

Full document: [project-5-group-4-grc-virtual-lab.pdf](project-5-group-4-grc-virtual-lab.pdf) (70 pages)

## Context

Group 4 loaded three demonstration datasets in the GRC Practice Lab and configured risk appetite, key risk indicators, business impact analysis, the risk register, risk treatment, and cloud risk scenarios.

The report states that the results are demonstration findings from the lab, not independent audits of real organisations. The three datasets are:

1. **CloudPay** — a fictional New York fintech with about 120 employees, digital payments, and stated obligations that include PCI DSS, SOC 2, ISO 27001, and GDPR.
2. **MediChart** — a fictional healthcare SaaS provider handling patient information, with HIPAA in view.
3. **SaaSCo** — an enterprise GRC portfolio spanning several risk categories and cloud environments.

## Role

Contributing member of Group 4. The published report is the group's joint product.

## Frameworks and methods

Used in the lab and discussed in the report:

- Risk appetite statements, including averse, cautious, moderate, open, and hungry positions, and whether statements were board-approved.
- Key risk indicators, marked Healthy, Warning, or Breached.
- Business impact analysis using recovery time objective (RTO), recovery point objective (RPO), and maximum tolerable period of disruption (MTPD).
- A risk register scored by likelihood and impact.
- Four treatment strategies: mitigate, accept, avoid, and transfer. The comparison counts plans as Completed, In Progress, or Planned.
- Cloud risk scenarios for AWS, Azure, Google Cloud Platform, and multi-cloud setups inside the same lab.

ISO 27001 appears as one of CloudPay's stated compliance obligations in the demonstration data. The report does not present an ISO 27001 audit.

## Deliverables and findings

The group's comparison tables report:

| | CloudPay | MediChart | Enterprise portfolio |
| --- | --- | --- | --- |
| Risk appetite statements | 8 (5 board-approved) | 9 (all 9 board-approved) | 21 |
| KRIs | 7 (3 Healthy, 3 Warning, 1 Breached) | 8 (3 Healthy, 4 Warning, 1 Breached) | 21 (18 Healthy, 1 Warning, 2 Breached) |
| Risks in the register | 15 (1 Critical, 8 High, 6 Medium, 0 Low) | 16 (1 Critical, 6 High, 8 Medium, 1 Low) | 21 |
| Treatment plans | 9 (0 completed, 0%) | 10 (1 completed, 10%) | 21 (0 completed, 0%) |
| Cloud scenarios | 12 (3 Critical, 7 High) | 12 (4 Critical, 5 High, 3 Medium) | 21 (all High or Critical) |

The executive summary gives the same treatment picture for CloudPay: nine plans, none completed. It also records a CloudPay ransomware risk scored 20 out of 25, and a KRI for two critical vulnerabilities still unremediated after seven days.

CloudPay business impact analysis, as entered by the group:

| Process | Criticality | RTO | RPO | MTPD |
| --- | --- | --- | --- | --- |
| Payment Processing | Critical | 1 hour | 1 hour | 4 hours |
| Merchant Portal and Customer Access | High | 4 hours | 2 hours | 12 hours |
| Corporate Communication and Collaboration | Medium | 4 hours | 4 hours | 20 hours |

The group calculated the gap between RTO and MTPD as 3 hours, 8 hours, and 16 hours for those three processes. They also noted that an operational appetite statement quoted a 15-minute RPO while Payment Processing was recorded with a one-hour RPO, and that the two figures needed to be reconciled.

The closing observation in the report is that appetite statements, KRIs, and treatment plans were documented while completion stayed at 0% for CloudPay and the enterprise portfolio, and 10% for MediChart.

## Skills demonstrated

Joint GRC lab work: risk appetite, KRIs, business impact analysis, risk registers, treatment plans, and cloud risk scenarios on demonstration data. This is a team training exercise, not a claim of cloud administration or audit experience in a live organisation.
