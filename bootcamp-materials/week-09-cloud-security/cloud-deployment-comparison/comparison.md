# Deployment comparison

| Deployment | Who runs the infrastructure | A plain example | Security consequence |
| --- | --- | --- | --- |
| Public | A provider, shared with other customers | A mailbox or a lab account at a large provider | You share the platform. Isolation, identity, and their physical controls matter. Confirm the region and the contract |
| Private | One organisation | The VirtualBox host-only lab on your laptop | You hold the hardware and the mistakes. Nobody else patches the laptop for you |
| Hybrid | Both, joined on purpose | Identity in a public service, logs still on the Wazuh VM | The join is a new boundary. Keys, network paths, and "which side logged this?" become the design |

## My choices

| Workload | Deployment I would pick | Why | Risk I accept by picking it |
| --- | --- | --- | --- |
| School or bootcamp mailbox |  |  |  |
| Wazuh manager for this portfolio | Private, on the laptop, unless I write a different plan | The course lab is local and the RAM is on the laptop | The laptop can be lost or full |
