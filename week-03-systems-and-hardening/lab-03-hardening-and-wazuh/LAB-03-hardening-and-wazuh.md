::: title-page
# Lab 03 — Hardening, Sysmon, and Wazuh

**Course:** Maxim Nyansa Cybersecurity Bootcamp, Ghana  
**Trainee:** James Ackah Blay · Aiyinasi, Ghana  
**Week:** 3 — Computer systems and secure workstations  
**Estimated time:** 6 hours, split across two sittings if the indexer is slow  
**Difficulty:** Intermediate. You leave this lab with a manager and one agent, or with an honest note about what failed.

::: tutor
**Tutor note.** The audit script only reads. Do not add an "apply fixes" mode. Install Wazuh from the current official quickstart, then record the version you actually installed. Service names below are the usual Wazuh 4.x all-in-one names. If a unit is missing, use the names in the guide you followed.
:::
:::

## 1. Learning objectives

| Objective | Job skill |
| --- | --- |
| Run a read-only baseline and explain each result | Endpoint hardening without breaking a host |
| Install a SIEM manager and enrol one Windows agent | Stand up the sensor path a SOC shift depends on |
| Generate one Sysmon event and find it | Prove a detection has a log behind it |
| Test a restore, not only a copy | Say whether a backup is real |

## 2. Prerequisites and setup

Week 2 addresses: Ubuntu at `192.168.56.10`, Windows at `192.168.56.20`. Raise the Ubuntu VM to 8 GB RAM and 2 vCPU before the Wazuh indexer install. Keep Kali off. NAT may stay on for the install, then you can disable it.

Read `../../hardening-audit/README.md` and `../../home-soc-lab-windows-endpoint/sysmon-lab-config.xml`.

Official install, version you choose: [Wazuh quickstart](https://documentation.wazuh.com/current/quickstart.html).

## 3. Scenario

You joined a small security team on a Monday. The previous person left a laptop and a promise that "logging is sorted". Your job this week is to make one Ubuntu manager and one Windows endpoint produce an event you can point at. A dashboard you have not logged into is not evidence.

## 4. Tasks

### Task 1 — Read-only audit on Ubuntu

```bash
cd week-03-systems-and-hardening/hardening-audit
python3 hardening_audit.py --root /
```

Save the text to `evidence/ubuntu-audit.txt` inside that project, or in this lab folder if you prefer one place. `skip` means the file was not readable. It is not a pass.

On Windows:

```powershell
powershell -ExecutionPolicy Bypass -File .\audit-windows.ps1
```

Run that from `hardening-audit` on the Windows VM. Save the transcript.

::: checkpoint
**You should now see** a line for SSH root login, shadow permissions, and a summary of pass, fail, review, and skip. Root login should not be `yes`. If it is, set `PermitRootLogin no` in `sshd_config`, reload `ssh`, and re-run the audit. Do not turn the script into something that edits the file for you.
:::

### Task 2 — Install Wazuh all-in-one

Follow the official quickstart on the Ubuntu VM. Record:

```bash
# After install. Names may differ. Write the names you have.
systemctl is-active wazuh-indexer wazuh-manager wazuh-dashboard
```

Sign in to the dashboard from the laptop over the lab path the guide requires. Do not publish the dashboard to the internet. Screenshot your own login, with the version visible if the UI shows it. Write the version in `install-notes.md`.

If the indexer is killed or the UI never loads, check memory:

```bash
free -h
sudo journalctl -u wazuh-indexer -n 40 --no-pager
```

Stop other guests. 8 GB is a student start, not a vendor sizing study.

### Task 3 — Sysmon, then the agent

On Windows, install Sysmon only from Microsoft Sysinternals. From an elevated prompt, in the folder that contains `sysmon-lab-config.xml`:

```bat
sysmon64.exe -accepteula -i sysmon-lab-config.xml
sc query Sysmon64
```

If Sysmon complains about `schemaversion`, set that attribute to the version `sysmon64.exe -?` implies and install again. The lab config logs process creation and network connections. It is noisy. It stays on this VM.

Install the Wazuh Windows agent from the current Wazuh documentation. Manager address: `192.168.56.10`.

::: checkpoint
**You should now see** the agent listed as active in the dashboard you are looking at. Write the agent id in `install-notes.md`. An empty agent list is an honest early state. Do not type an id you have not seen.
:::

### Task 4 — Generate one event

On Windows, open Notepad, or:

```powershell
notepad.exe
```

Give the dashboard a minute. Find a process-create event for Notepad, or say which filter you used and that it had not arrived yet. Quote one field you saw: time, image path, or user. Do not invent the field.

### Task 5 — Prove a backup

Copy one small file to a second disk or to the host. Delete only the copy's destination test. Restore it. Compare size or a hash:

```bash
sha256sum the-file the-restored-file
```

A backup you have not restored stays a gap on the Week 3 checklist.

## 5. Troubleshooting

| What you see | What to try |
| --- | --- |
| Indexer restart loop | RAM. `free -h`. Close other VMs. Read the unit log before you reinstall |
| Agent never becomes active | Windows firewall, manager IP not `192.168.56.10`, or the agent enrolled to the NAT address |
| Dashboard times out | You are using the VM's NAT address from a place that cannot reach it. Use the host-only address or the port forward the guide documented |
| Sysmon service missing | The install did not finish. Re-run from an elevated prompt and read the printed error |
| Audit says `skip` on shadow | You are not root and cannot stat the file. Say so. Do not chmod the file to make the check pass |

## 6. Stretch task

Write one sentence a senior analyst could drop into a shift handover: which host, which agent id, which event, what time. If any of those four is missing, the handover says what is missing.

## 7. Evidence

- Audit text from Ubuntu and the Windows script output.
- Wazuh version, dashboard screenshot, agent id.
- One Sysmon or Wazuh event you generated.
- Restore hashes, or a note that the restore has not been done.

## 8. Reflection

1. Which audit result did you disagree with, and what did you do?
2. What broke when RAM was tight?
3. What would you tell a teammate who wants the audit script to "just fix SSH"?

## 9. Interview questions

1. Why is a world-readable shadow file a problem?
2. What is the difference between a manager and an agent?
3. Why do you test a restore?
4. What does Sysmon add that Windows security events do not?
5. How do you prove an agent is enrolled without inventing an id?

## 10. Grading rubric

| Criterion | Exceeds | Meets | Not yet |
| --- | --- | --- | --- |
| Baseline | You changed one setting and re-ran the audit | Both audits were run and saved | The unit-test output was pasted as the server |
| Wazuh | Version, screenshot, and active agent id are yours | Manager is installed and the gap is written if the agent is not active | A copied dashboard from the internet |
| Event | One real process or network event is quoted | You tried and recorded the filter | "It works" with no field |
| Backup | Hashes match after a restore | A copy exists and you say it is untested | No note |
