::: title-page
# Lab 02 — Packets, subnets, and the lab network

**Course:** Maxim Nyansa Cybersecurity Bootcamp, Ghana  
**Trainee:** James Ackah Blay · Aiyinasi, Ghana  
**Week:** 2 — TCP/IP networking  
**Estimated time:** 4 hours  
**Difficulty:** Foundation. You will build the network every later lab uses.

::: tutor
**Tutor note.** Capture only traffic on your VirtualBox host-only network. Do not point a capture at the family router or a school network. Write down the interface name you actually have. Do not copy an interface name from this page if `ip` shows a different one.
:::
:::

## 1. Learning objectives

| Objective | Job skill |
| --- | --- |
| Give the three lab machines stable addresses | Build a range you can defend later |
| Explain one TCP handshake from a capture | Read a flow instead of guessing from a port number |
| Calculate a /24 by hand and with the Week 2 script | Stop mis-scoping a subnet in a ticket |
| Say which NIC a packet used | Know whether an alert came from the lab or the home LAN |

## 2. Prerequisites and setup

VirtualBox on the 32 GB laptop. Create a host-only network. VirtualBox often uses `192.168.56.1/24` on the host. If yours differs, change the plan, do not force the document.

| Machine | Address | When |
| --- | --- | --- |
| Host-only adapter | 192.168.56.1 | This week, if VirtualBox chose that |
| wazuh (Ubuntu Server) | 192.168.56.10 | Create the VM this week. Wazuh itself is Week 3 |
| win-endpoint | 192.168.56.20 | Create the VM this week if RAM allows |
| kali | 192.168.56.30 | Do not create it until Week 10 |

Leave at least 12 GB for the laptop. Give the Ubuntu VM 2 vCPU, 4 GB RAM for now, and 50 GB disk. You will raise it toward 8 GB in Week 3 when the indexer is installed. Adapter 1 is host-only. Adapter 2 may be NAT for updates, and you will disable NAT during later assessment weeks.

Tools on Ubuntu: `iproute2` and `tcpdump`. On the laptop: Wireshark. Both are observers. They are not scanners of someone else's network.

Also use `week-02-tcp-ip-networking/addressing-practice/net_addressing.py`.

## 3. Scenario

You are the junior analyst who will own a small SOC lab. Before any detection tool exists, you must prove that `win-endpoint` can reach `wazuh` and that this traffic cannot be confused with the house LAN. A later incident report will be worthless if the addresses were never written down.

## 4. Tasks

### Task 1 — Name the interfaces

On the Ubuntu VM:

```bash
ip -br addr
ip route
```

Write the host-only interface name in your notes. It might be `enp0s3`, `enp0s8`, or `eth0`. The NAT interface, if present, has a different address, often in `10.0.2.0/24`.

::: checkpoint
**You should now see** one address in `192.168.56.0/24` and, if NAT is attached, a second address that is not in that range. If you see only a NAT address, the host-only adapter is not connected. Fix that in the VM settings and reboot.
:::

### Task 2 — Set a static address

On Ubuntu Server with netplan, identify the file under `/etc/netplan/`. Edit a copy of the host-only NIC only. Example, which you must change if the NIC name differs:

```yaml
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: false
      addresses:
        - 192.168.56.10/24
```

Then:

```bash
sudo netplan apply
ip -br addr show
ping -c 3 192.168.56.1
```

On Windows, set the host-only adapter to `192.168.56.20`, mask `255.255.255.0`, and no default gateway on that adapter. Leave the gateway on the NAT adapter if you still want updates. In an elevated PowerShell:

```powershell
Get-NetIPAddress -AddressFamily IPv4 | Format-Table InterfaceAlias, IPAddress, PrefixLength
```

::: checkpoint
**You should now see** `192.168.56.10/24` on Ubuntu and `192.168.56.20/24` on Windows. `ping 192.168.56.10` from Windows should receive replies. If it does not, check that both adapters are the host-only network, not Bridged.
:::

### Task 3 — Subnet the plan by hand, then check it

Answer in `worksheet.md` in this folder, then check with:

```bash
python3 ../../addressing-practice/net_addressing.py 192.168.56.10/24
```

You are confirming the network address, the broadcast address, and whether `.10` and `.20` share the /24. Do the arithmetic before you run the script.

### Task 4 — Capture one handshake

From Ubuntu, while Windows pings or opens an SSH attempt you will abandon:

```bash
sudo tcpdump -i enp0s3 -n -c 30 'host 192.168.56.20 and tcp'
```

Replace `enp0s3` with the interface from Task 1. Start the capture, then from Windows:

```powershell
Test-NetConnection 192.168.56.10 -Port 22
```

SSH may refuse the connection. That is fine. You want the packets, not a login.

In Wireshark on the laptop, capture the host-only adapter if you prefer a GUI. Filter:

```text
ip.addr == 192.168.56.10 && tcp.port == 22
```

A TCP handshake is SYN, then SYN-ACK, then ACK. A refused port is often SYN then RST.

Save the tcpdump text, not a huge pcap of the house, into this folder only if it contains lab addresses. Run the summary helper on a text capture:

```bash
python3 tcpdump_summary.py your-capture.txt
```

A synthetic sample is in `samples/lab-handshake.txt` so you can learn the script before your VM exists. Label your file `my-lab` in the notes. The sample is not your capture.

::: checkpoint
**You should now see** three lines that show who sent the SYN, who answered, and the flags. Your notes name the interface. A capture that only shows `10.0.2.15` is the NAT adapter. Capture the host-only NIC instead.
:::

### Task 5 — Write the network map

Update `../../home-soc-lab-network/address-plan.csv`. Change a row from `planned` to `built` only after you have read the address on that machine. Paste the `ip` or PowerShell output path in your evidence note.

## 5. Troubleshooting

| What you see | What it usually means |
| --- | --- |
| Ping works to `.1` and not to the other VM | The other VM is on NAT or is powered off |
| Two VMs have the same address | Duplicate static configuration. Fix one before you install Wazuh |
| `tcpdump: enp0s3: No such device` | Use the name from `ip -br addr` |
| Capture is empty | The filter interface is the wrong NIC, or no traffic was sent during the 30 packets |
| Wireshark shows the home SSID | You selected the wrong adapter. Close it. Do not save that file into git |

## 6. Stretch task

Add a second host-only test: can Ubuntu reach `192.168.56.20` on TCP 445 without you having enabled anything? Record the flags only. Then explain, in two sentences, why that port matters to a later Windows log and why you will not leave it facing the house LAN.

## 7. Evidence

- `ip -br addr` output from Ubuntu.
- The PowerShell address table from Windows.
- A short tcpdump or Wireshark note that quotes three lines you captured, or a clear statement that the VM is not built yet.
- The address plan with `built` only on rows you observed.

## 8. Reflection

1. Which address is the host, and which is a guest?
2. What would break in Week 3 if the Wazuh VM got its address from DHCP and the address changed?
3. Why is a NAT address a poor address to write into a detection rule?

## 9. Interview questions

1. What is the network address of a /24, and why are there 254 usable hosts?
2. What do SYN, SYN-ACK, and ACK tell you?
3. How can you tell a capture was taken on the wrong interface?
4. Why do analysts care which subnet an IP belongs to before they escalate?

## 10. Grading rubric

| Criterion | Exceeds | Meets | Not yet |
| --- | --- | --- | --- |
| Addressing | Static addresses match the plan and you calculated the /24 before the script | Both VMs answer on the host-only network, or you documented the blocker | Bridged the lab onto the home LAN |
| Capture | You explain a real handshake or RST from your NIC | You ran tcpdump on the lab NIC and kept the output | You submitted only `samples/lab-handshake.txt` as if you captured it |
| Map | `built` rows match command output | The plan is updated honestly | Every row says built with no output |
