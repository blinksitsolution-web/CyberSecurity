# Tutor answer key — Lab 03

Not part of the trainee PDF.

There is no universal audit output. Mark the lab from his files:

- `PermitRootLogin` should not be `yes` after he finishes. The read-only script must not have been changed to edit the system.
- Wazuh version, a screenshot he took, and an agent id he can point to in the UI. A missing agent is acceptable only with the log line that shows why.
- One quoted event field (time, path, or user) for a process he started, such as Notepad.
- Two hashes that match, or a written statement that the restore was not done.

Service names `wazuh-indexer`, `wazuh-manager`, and `wazuh-dashboard` are the usual 4.x all-in-one units. If his guide used other names, those names are the answer.
