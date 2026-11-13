# Tutor answer key — Lab 02

Not part of the trainee PDF.

Worksheet answers for the planned network:

1. Network address `192.168.56.0`.
2. Broadcast `192.168.56.255`.
3. 254 usable hosts. The first address names the network and the last is the broadcast.
4. Yes, `.20` is in that /24.
5. The interface name must come from his `ip -br addr`, not from the guide's example `enp0s3`.
6. and 7. Only his command output counts. `samples/lab-handshake.txt` is synthetic: SYN, SYN-ACK, ACK from `.20` to `.10` port 22.

`tcpdump_summary.py` on that sample prints `packets=3` and flags `S`, `S.`, and `.`.

A bridged adapter or a capture of the home LAN does not meet the lab.
