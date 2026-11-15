# GRC Practice Lab: control register, control mapping and control lifecycle

Individual write-up by James Ackah-Blay. The file properties record 8 October 2026, during Week 1 of the Maxim Nyansa bootcamp (5–9 October 2026).

Full document: [grc-practice-lab-control-register-mapping-and-lifecycle.pdf](grc-practice-lab-control-register-mapping-and-lifecycle.pdf)

## Context

The exercise uses a GRC Practice Lab dashboard that shows a risk register, a control register, treatment records, and a six-stage control lifecycle. James read the counts on that dashboard and wrote up what they do, and do not, show.

## Role

He completed this as an individual practice lab. The write-up is in the first person and the file author is James Ackah Blay.

## Frameworks and methods

The write-up names the NIST Cybersecurity Framework 2.0 as an example of a framework that control mapping can point to. It also says a separate control-register screenshot would be needed to verify that ten new controls were added and mapped to at least two frameworks each. That screenshot is not in the document, so this case study does not treat a finished control-to-framework mapping as delivered work.

The method he did apply is reading a GRC dashboard: lifecycle stage, maturity score, owner, and review date.

## Deliverables and findings

The dashboard counts he recorded:

| Item | Count |
| --- | --- |
| Risk register | 12 |
| Controls | 35 |
| Treatments | 4 |
| Control lifecycle records | 6, one control in each stage |

The six lifecycle examples, with the maturity scores printed in the write-up:

| Stage | Control | Maturity |
| --- | --- | --- |
| Proposed | Encrypted backups with quarterly restore testing | 1/5 |
| Designed | Review user access rights and enforce least-privilege permissions | 2/5 |
| Implemented | Security awareness training and phishing simulations | 2/5 |
| Operating | Multi-factor authentication for privileged and customer-facing access | 1/5 |
| Monitoring | Centralized SIEM with 24/7 monitoring and alerting | 1/5 |
| Retired | Legacy FTP file transfer restriction | 3/5 |

He calculated the average of those six displayed scores as 1.67 out of 5. Three scores are 1/5, two are 2/5, and one is 3/5.

Review dates he copied from the dashboard include 30 October 2026 (user-access review and centralized SIEM), 15 November 2026 (multi-factor authentication), 1 December 2026 (security awareness training), and 1 September 2026 (proposed encrypted backups). He noted that, against the write-up date of 8 October 2026, the 1 September 2026 backup review was already overdue.

He also wrote that the six lifecycle rows should not be treated as all 35 controls, and that the counts alone do not show whether every risk has a control or whether the four treatments reduced risk.

## Skills demonstrated

Reading a GRC control lifecycle, separating a lifecycle stage from a maturity score, checking review dates, and stating the limit of a screenshot. The unfinished item he recorded himself is evidence of ten added controls and their framework mappings.
