# Home SOC lab network

## Goal

Design the VirtualBox network you will reuse from Week 3 through the capstone. This is a separate project from the general network map so the lab has one address plan.

The laptop has 32 GB of RAM. The lab is three guests over time: Ubuntu Server for Wazuh, a Windows endpoint with Sysmon and a Wazuh agent, and Kali added only in Week 10 for authorised work.

## What was built

- `lab-network.md` — purpose, RAM budget, and rules.
- `address-plan.csv` — names and addresses. Status stays `planned` until you build the VM.

## How to reproduce

1. In VirtualBox, create a host-only network. The usual address of the host adapter is `192.168.56.1/24`. If yours differs, change the CSV rather than forcing the document to be right.
2. Do not bridge the lab machines onto the network you share with other people.
3. When a VM exists, change its row from `planned` to `built` and paste the command output that shows the address into `evidence/`.

You are not installing Wazuh or Kali this week. Those steps live in Week 3 and Week 10.

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
