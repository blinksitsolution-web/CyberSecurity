# Home SOC lab — Windows endpoint

## Goal

Build the endpoint that will generate the logs a SOC analyst practises on: Windows, Sysmon, and a Wazuh agent talking only to your manager.

## What was built

- `windows-endpoint-plan.md` — install order and evidence prompts.
- `sysmon-lab-config.xml` — a small lab config that logs process creation and network connections. It is noisy. It is for this VM, not a production image.

No agent id is filled in. That number comes from your dashboard.

## How to reproduce

1. Create the Windows VM: 4 GB RAM, host-only address `192.168.56.20`.
2. Apply Windows updates and record the date.
3. Install Sysmon from the official Microsoft Sysinternals page only. Then, in an elevated prompt, from the folder that contains your config:

```bat
sysmon64.exe -accepteula -i sysmon-lab-config.xml
```

If Sysmon warns about `schemaversion`, set that attribute to the version your binary expects and run the install again. Confirm the service is running. Do not download Sysmon from a random mirror.

4. Install the Wazuh Windows agent from the current Wazuh documentation, with the manager address `192.168.56.10`.
5. In the dashboard, confirm the agent is active. Screenshot your own screen into `evidence/`.
6. Run `../hardening-audit/audit-windows.ps1` and attach that output to the baseline.

## Evidence to add yourself

Do not invent results. Fill these lines only with what you did.

- Date completed:
- What you did:
- File in `evidence/`:
- Feedback:

## What I learned

Answer in your own words.

1. What was this deliverable for?
2. What is finished, and what is still open?
3. What is clearer than it was at the start of the week?
4. What would you do on a SOC shift because of this?
5. Which evidence file is yours?
