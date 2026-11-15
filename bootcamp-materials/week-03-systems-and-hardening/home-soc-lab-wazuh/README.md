# Home SOC lab — Wazuh on Ubuntu Server

## Goal

Stand up the manager that later weeks send logs to. This is the detection platform for the capstone. You install it on your own Ubuntu VM, on the address planned in Week 2.

## What was built

`wazuh-server-plan.md` is a lab plan: resources, order of work, and the evidence to keep. It points at the current Wazuh quickstart instead of freezing a command that will go stale. No dashboard screenshot is included, because this repository has not installed Wazuh.

## How to reproduce

1. Create the Ubuntu Server VM from the Week 2 plan: 8 GB RAM, host-only `192.168.56.10`, optional NAT for the install only.
2. Follow the current all-in-one quickstart: [Wazuh documentation quickstart](https://documentation.wazuh.com/current/quickstart.html).
3. Record the version you actually installed. Service names in the 4.x all-in-one guide are often `wazuh-indexer`, `wazuh-manager`, and `wazuh-dashboard`. If a name differs, trust the guide you used.
4. Confirm status with the read-only commands in the plan, and save the output.
5. Take a snapshot called something you will recognise, such as `wazuh-installed`.

Do not expose the dashboard to the internet. Reach it from the laptop, over the host-only or NAT path the guide requires.

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
