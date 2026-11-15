# Packet Tracer and Wireshark network lab

Individual Friday review lab by James Ackah-Blay, Week 2 of the Maxim Nyansa bootcamp (TCP/IP networking, 12–16 October 2026). The session is the Friday 16 October 2026 review: three labs in Cisco Packet Tracer, Wireshark, and command-line network utilities.

Adepa Logistics is a fictional training network. This page describes the tasks in that lab. It does not quote command output, packet counts, or screenshots. Those files are not in this folder yet.

## Scenario

Adepa Logistics has the head-office block `192.168.50.0/24`, split into four `/26` subnets (mask `255.255.255.192`). Three zones are built. The fourth is reserved.

| Zone | Network | Gateway | Usable hosts | Broadcast |
| --- | --- | --- | --- | --- |
| Admin | `192.168.50.0/26` | R1 Gi0/0 `192.168.50.1` | `.1`–`.62` | `192.168.50.63` |
| Warehouse | `192.168.50.64/26` | R1 Gi0/1 `192.168.50.65` | `.65`–`.126` | `192.168.50.127` |
| Guest (reserved) | `192.168.50.128/26` | not used in this lab | `.129`–`.190` | `192.168.50.191` |
| Servers | `192.168.50.192/26` | R1 Gi0/2 `192.168.50.193` | `.193`–`.254` | `192.168.50.255` |

Static addresses in the plan: PC-WH1 `192.168.50.70`, PC-WH2 `192.168.50.71`, SRV-Web `192.168.50.200`. Each uses mask `255.255.255.192`. Warehouse PCs use gateway `192.168.50.65`. The server uses gateway `192.168.50.193`. DNS for those devices is `192.168.50.200`.

The Admin DHCP pool is named ADMIN. Addresses `192.168.50.1` through `192.168.50.10` are excluded. The pool is network `192.168.50.0` `255.255.255.192`, default router `192.168.50.1`, DNS server `192.168.50.200`, and it hands out addresses from `.11` upward. PC-Admin1 and PC-Admin2 take an address from that pool.

## Role

James completed the lab on his own machine and in Packet Tracer, capturing only his own interface. A later pair exercise swaps a faulty copy with a classmate. No classmate is named here.

## Tools

- Cisco Packet Tracer, for the router, switches, PCs, server, DHCP, DNS, HTTP, the access list, and Simulation mode
- Wireshark, for a capture of his own traffic and for display filters, capture filters, and conversation statistics
- Windows PowerShell and Linux command-line utilities for the local interface, ARP, routing, connection, and DNS tables, plus the lab’s read-only network health-check script

## What was built and analysed

**Packet Tracer.** One router (R1) with three Gigabit Ethernet links, three 2960 switches (SW-Admin, SW-WH, SW-Srv), four PCs, and one server (SRV-Web). Straight-through copper links connect each switch to a router interface and the end devices to the switches. SRV-Web serves HTTP and a DNS A record for `www.adepa.test` pointing at `192.168.50.200`.

Checks used on the finished network: `ping` and `tracert` between zones, a browser request to `http://www.adepa.test`, and on R1 the commands `show ip route`, `show arp`, `show ip dhcp binding`, and `show ip interface brief`. On SW-WH, `show mac address-table`. In Simulation mode he stepped through DHCP (Discover, Offer, Request, Acknowledge), then DNS, the TCP handshake, and HTTP.

**Access list.** An extended ACL named `WH_IN` is applied inbound on R1 GigabitEthernet0/1. The Warehouse subnet `192.168.50.64/26` (wildcard `0.0.0.63`) may send DNS (UDP 53) and HTTP (TCP 80) to `192.168.50.200`, and ICMP to the Servers subnet `192.168.50.192/26`. Other IP traffic from that interface is denied. The list is read top to bottom and the first match wins. `show access-lists` is the check. The lab’s expected tests are that the warehouse web page still loads and that a ping from a Warehouse PC into the Admin zone is blocked.

**Troubleshooting.** A second Packet Tracer file is saved and three faults are injected from the lab menu, then swapped. Diagnosis follows six steps: identify the symptom, establish the scope, test connectivity, isolate the cause, correct and verify, and document. Which faults were injected, and the log of tests, are not in this repository.

**Wireshark.** Captures stay on his own interface. Protocols examined on the core path:

- ARP: request to the broadcast MAC, reply unicast, compared with the local ARP table
- DNS: name lookup, A and AAAA records, TTL, and UDP port 53
- ICMP: echo requests, and type 11 Time Exceeded messages while running traceroute, with the TTL on the probes
- TCP: the handshake flags on a training HTTP login to the class server
- TLS: the Client Hello, including the server name, against encrypted application data

Display filters select packets already captured (`arp`, `dns`, `icmp`, `icmp.type == 11`, `tcp.port == 8000`, `tls.handshake.type == 1`). A capture filter limits what is recorded. The lab also builds a flow view in Statistics → Conversations: a flow is the five-tuple of source IP, destination IP, source port, destination port, and protocol, with packet and byte counts. That is the same idea as a NetFlow record. The guide’s router NetFlow commands are reference only and are not treated here as output from Packet Tracer.

**Command-line utilities.** The core stations read five local tables and save a health-check report:

| Station | Table | Commands the lab uses |
| --- | --- | --- |
| 1 | Interfaces | `ipconfig /all`, `Get-NetIPConfiguration`; Linux `ip -br addr` |
| 2 | MAC-to-IP (ARP / neighbour) | `arp -a`, `Get-NetNeighbor`; Linux `ip neigh show` |
| 3 | Routing | `route print -4`, `Get-NetRoute`; Linux `ip route` |
| 4 | Connections and listeners | `netstat -ano`, `Get-NetTCPConnection`; Linux `ss` |
| 5 | DNS cache and lookups | `ipconfig /displaydns`, `nslookup`, `Resolve-DnsName`; Linux `dig` |

The health-check script is read-only. It writes interface, ARP, route, DNS, listening-port, and reachability sections to a text file. The saved report is not in this folder.

## Skills demonstrated

Subnetting a `/24` into `/26` networks, static and DHCP addressing, default gateways, DNS and HTTP on a server, an extended ACL, and a six-step fault log. Reading DHCP, ARP, DNS, TCP, ICMP, and TLS in Packet Tracer Simulation mode and in Wireshark. Telling a display filter from a capture filter, and summarising a capture as flows. Reading the interface, ARP, routing, connection, and DNS tables from Windows or Linux.

## EXIN Cyber & IT Security Foundation

The lab cover assigns the session to topics 1.1 and 1.2, plus troubleshooting and defence terms from the basic concept list.

| Topic | What this lab practises |
| --- | --- |
| 1.1 Nodes, node connections, and TCP/IP addressing | Routers, switches, PCs, and a server as nodes; copper links; IPv4 addresses, masks, gateways, and the `/26` plan |
| 1.2 OSI and TCP/IP models, and protocols | ARP, DNS, DHCP, ICMP, TCP, HTTP, and TLS, and where each appears in a capture or a router table |

The access list and the timeout-versus-refusal capture are the defence and troubleshooting terms the cover adds to those two topics. This lab is bootcamp practice. It is not an EXIN certificate.

## Evidence

Packet Tracer file, capture screenshots and answers will be added.
