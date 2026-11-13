# Lab network plan

## Machines

| VM | Role | When it appears | Suggested RAM | Suggested disk |
| --- | --- | --- | --- | --- |
| `wazuh` | Ubuntu Server, Wazuh all-in-one | Week 3 | 8 GB | 50 GB |
| `win-endpoint` | Windows endpoint, Sysmon, Wazuh agent | Week 3 | 4 GB | 60 GB |
| `kali` | Authorised assessment only | Week 10 | 4 GB | 40 GB |

If all three run at once, 8 + 4 + 4 = 16 GB for guests. Leave at least 12 GB for the laptop itself, and close Kali when you are not in an authorised lab. Wazuh's indexer is the hungry service. If the Ubuntu VM swaps constantly, stop Kali and give Wazuh the memory back. These numbers are a starting plan, not a benchmark from your machine.

## Adapters

- Adapter 1: host-only, on `192.168.56.0/24`, for lab traffic.
- Adapter 2, optional: NAT, for updates only. Disable it during an assessment so tools are not sitting on a path to the wider network.

## Rules that stay in force

- The scope file in Week 10 names what you may test. Until then, build and harden. Do not attack the VMs.
- Snapshots: take one before a risky change, and write the snapshot name in your evidence note.
- Sample logs later in Week 11 are synthetic. Your VM logs are yours. Keep personal data out of git.
