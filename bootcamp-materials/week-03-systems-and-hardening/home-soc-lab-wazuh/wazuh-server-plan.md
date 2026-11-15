# Wazuh server plan

- Planned address: `192.168.56.10`
- Operating system: current Ubuntu Server LTS
- Role: all-in-one Wazuh manager, indexer, and dashboard for one Windows agent
- Version installed: [fill from the VM]
- Snapshot name:

## Order

1. Install Ubuntu and apply updates. Record the date.
2. Set the host-only address. Confirm it from the VM, then paste that output.
3. Install Wazuh from the official quickstart for the version you chose.
4. Sign in to the dashboard from the laptop. Save a screenshot you took yourself into `evidence/`.
5. Leave the agent enrolment for the Windows project. An empty agent list is an honest early screenshot.

## Read-only checks

Run these on the Ubuntu VM after install. If a unit name is not found, write the names your guide used.

```bash
systemctl status wazuh-indexer wazuh-manager wazuh-dashboard --no-pager
```

Paste the output under Evidence in the README. Do not type a healthy status from memory.

## If the VM is too slow

Stop other guests. The indexer wants memory. 8 GB is a student starting point, not a vendor sizing exercise. Write down what you observed: swapping, a service that failed, or a dashboard that did not load.
