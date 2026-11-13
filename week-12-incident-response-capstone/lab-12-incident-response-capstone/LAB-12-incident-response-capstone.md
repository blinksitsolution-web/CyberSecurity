::: title-page
# Lab 12 — Incident simulation and capstone

**Course:** Maxim Nyansa Cybersecurity Bootcamp, Ghana  
**Trainee:** James Ackah Blay · Aiyinasi, Ghana  
**Week:** 12 — Incident response and capstone  
**Estimated time:** 8 hours  
**Difficulty:** Capstone. You will run a small incident on machines you own, write it up, and say what a three-month analyst still would not claim.

::: tutor
**Tutor note.** Authorisation: the only "adversary" in this lab is you, on `192.168.56.10` and `192.168.56.20`. You create a noisy login failure and a lab admin account, then you respond. You do not attack another network, and you do not follow an exploit guide. If the VMs are not built, complete the paper timeline on the synthetic alerts from Lab 11 and label it PRACTICE DATA.
:::
:::

## 1. Learning objectives

| Objective | Job skill |
| --- | --- |
| Triage before you name an incident | The first ten minutes of a shift |
| Contain without deleting evidence | Disable an account, keep the logs, snapshot first |
| Recover and show what "normal" is | A restore or a removed lab account, with proof |
| Write a report a non-author can follow | Incident communication |
| Present the capstone without invented metrics | A portfolio a hiring manager can trust |

## 2. Prerequisites and setup

Labs 02, 03, 08, and 11. The report template is `../incident-report/incident-report.md`. The playbook is `../incident-response-notes/ir-playbook.md`. The capstone slides are `../capstone-outline/outline.md`.

Take a VirtualBox snapshot of the Ubuntu VM before Task 2. Name it `before-lab-12`.

## 3. Scenario

Monday 09:00. The dashboard, or the Lab 11 fixture if that is all you have, shows many failed logons and a new administrator. Nobody in your notes remembers approving the account. You have until the end of the sitting to decide, contain, preserve, remove, and write.

## 4. Tasks

### Task 1 — Snapshot and clock

```bash
date -u
```

Write the snapshot name and the UTC time in `timeline.csv`. If the clock is wrong, fix NTP before you trust the timeline. A SOC report with drifting clocks is how a good case becomes an argument.

### Task 2 — Create the signals yourself

On the Ubuntu VM, from a normal user, fail an SSH login five times with a wrong password you invent for this exercise. Then:

```bash
sudo adduser lab12user
sudo usermod -aG sudo lab12user
```

Pick a throwaway password. Do not reuse a personal one.

On Windows, only if you did not already do Lab 08's live task, you may create and later delete a local admin. One host is enough.

::: checkpoint
**You should now see** either a Wazuh alert you can quote, or the commands above in your timeline with the statement that the alert has not arrived. Both are acceptable. A quoted alert you did not see is not.
:::

### Task 3 — Triage and contain

Fill `../incident-response-notes/ir-playbook.md`. Containment options that fit this lab: disable the lab account, keep the VM on the host-only network, do not delete `/var/log`.

```bash
sudo usermod -L lab12user
sudo snapshot-note
```

There is no `snapshot-note` command. Take the VirtualBox snapshot in the GUI and write the name. Do not wipe the disk.

### Task 4 — Preserve, eradicate, recover

Copy the relevant auth log lines to a file outside the VM only if they contain no personal data. Then:

```bash
sudo deluser --remove-home lab12user
sudo grep lab12user /etc/passwd || echo "account gone"
```

If `deluser` is the wrong tool for your Ubuntu, use the command the man page gives and record it. Confirm the account is gone. If you used a snapshot to roll back instead, say that and accept that the guest is back at `before-lab-12`.

### Task 5 — Report and capstone

Complete `timeline.csv` and check it:

```bash
python3 timeline_check.py timeline.csv
```

Write `../incident-report/incident-report.md`. If the only alerts are the Lab 11 fixture, the banner says PRACTICE DATA. If you generated the account, the banner says `my-lab`.

Fill the capstone outline with paths to real files. The limits slide must include one thing the lab cannot see.

The 40-question mock in `../mock-assessment/` is separate revision. Score it yourself after you try. Do not commit `my-answers.csv` if you want the score private.

## 5. Troubleshooting

| What you see | What it means |
| --- | --- |
| No alert after five failures | The agent or the rule threshold. Look at `auth.log` directly and say the SIEM missed it |
| `adduser` wants a password interactively | That is normal. Do not put the password in the report |
| Timeline check fails | A time is out of order, or a row has no source |
| You deleted the only snapshot | Stop. Say so in the report. Do not pretend you can roll back |

## 6. Stretch task

Write one paragraph a hiring manager could read: the detection, the containment, and the limit. No tool list longer than three names. No claim that you have three years of shift work. The labs are how you practise the work. They are not a job history.

## 7. Evidence

- Snapshot names.
- Timeline that passes `timeline_check.py`.
- Proof the lab account is gone, or that you reverted the snapshot.
- Incident report with the correct data label.
- Capstone outline with at least one "not collected" cell still honest.

## 8. Reflection

1. What did you almost delete that you needed?
2. Which earlier lab supplied the detection, and which supplied the control you wish you had?
3. What will you not claim in an interview?

## 9. Interview questions

1. Walk an incident from triage to lessons learnt.
2. Why do you snapshot or copy logs before you clean?
3. What is the difference between containment and recovery?
4. How do you label practice data so a reader is not misled?
5. Which MITRE techniques did this simulation touch, and what did you not prove?

## 10. Grading rubric

| Criterion | Exceeds | Meets | Not yet |
| --- | --- | --- | --- |
| Simulation | Live alert quoted and the account removed | Commands and a truthful "no alert yet" | A fictional attacker story |
| Timeline | Check passes and sources are named | Times and actions are present | Unordered or sourceless |
| Report | A stranger could see impact and limits | Data label is correct | Sample logs called a breach |
| Capstone | Limits slide is specific | Outline points at real files | Metrics you did not measure |
