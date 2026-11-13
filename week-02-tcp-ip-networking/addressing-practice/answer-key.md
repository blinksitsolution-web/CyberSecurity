# Answer key

Open this after the worksheet. The script checks the same IPv4 and IPv6 facts.

1. `192.168.56.0`
2. `192.168.56.255`
3. 254. The first address names the network and the last is the broadcast, so they are not hosts.
4. Yes.
5. No. `10.0.0.8` is in a different network.
6. Loopback.
7. Link-local.
8. Documentation. `2001:db8::/32` is for examples. Do not use it as a real office range.
9. A `/64` is the normal IPv6 LAN prefix and contains a very large number of addresses. People do not usually subtract two for network and broadcast the way they do in a small IPv4 subnet.
10. The Wazuh server in the home-lab plan. That address is a design until you configure it.
