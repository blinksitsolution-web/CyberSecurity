# Architecture notes

## Terms

| Term | Plain meaning | Why a defender cares |
| --- | --- | --- |
| CPU, memory, disk | The machine's work, short-term storage, and long-term storage | A full disk or a starved VM hides logs and breaks a restore |
| Process | A running program | Alerts often name a process, a user, and a parent process |
| User and kernel | Everyday programs, and the part of the OS that talks to hardware | A kernel weakness is more serious than a bug in one app |
| Account | An identity the OS will act for | A new admin account is a Week 11 detection |
| Service | A program that stays running | Wazuh, SSH, and Windows Defender are services you will check |
| Permission | Who may read or change a file or setting | World-writable files and a world-readable `shadow` file are audit checks |
| Log | A record of what a service noticed | If it is not logged, the later incident report has a hole |
| Network boundary | Where one trust zone ends | Host-only is a boundary. The home LAN is outside it |

## My machines

| Machine | CPU cores observed | RAM observed | OS and version observed | What I used to check |
| --- | --- | --- | --- | --- |
| Laptop |  |  |  |  |
| wazuh VM |  |  |  |  |
| win-endpoint VM |  |  |  |  |

## Boundaries I will defend

| Boundary | Inside | Outside | Control I will rely on |
| --- | --- | --- | --- |
| Lab network | 192.168.56.0/24 | Home LAN and the internet | Host-only adapter |
| Everyday account | Normal user | Local administrators | Least privilege, Week 8 |
| Logs | What the sensor recorded | What I wish it had recorded | Write down gaps instead of filling them in |
