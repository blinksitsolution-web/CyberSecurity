#!/usr/bin/env python3
"""Small IPv4 and IPv6 helpers for the Week 2 addressing practice.

This is a calculator for addresses you type in. It does not scan a network.
"""

from __future__ import annotations

import argparse
import ipaddress
import json


def describe_cidr(cidr: str) -> dict:
    """Describe one address with a prefix, such as 192.168.56.10/24."""
    interface = ipaddress.ip_interface(cidr.strip())
    network = interface.network
    usable = network.num_addresses
    if interface.version == 4 and network.prefixlen <= 30:
        usable = network.num_addresses - 2
    result = {
        "version": interface.version,
        "address": str(interface.ip),
        "network": str(network.network_address),
        "prefix": network.prefixlen,
        "num_addresses": network.num_addresses,
        "usable_hosts": usable,
    }
    if interface.version == 4:
        result["netmask"] = str(network.netmask)
        result["broadcast"] = str(network.broadcast_address)
    return result


def same_subnet(first: str, second: str, prefix: int) -> bool:
    """Return True when both addresses sit in the same prefix."""
    network = ipaddress.ip_network(f"{first}/{prefix}", strict=False)
    return ipaddress.ip_address(second) in network


def classify_ipv6(address: str) -> str:
    """Name the common IPv6 address type a beginner is asked to recognise."""
    ip = ipaddress.ip_address(address.strip())
    if not isinstance(ip, ipaddress.IPv6Address):
        raise ValueError("classify_ipv6 expects an IPv6 address")
    if ip == ipaddress.ip_address("::1"):
        return "loopback"
    if ip.is_link_local:
        return "link-local"
    if ip.is_multicast:
        return "multicast"
    if ip in ipaddress.ip_network("2001:db8::/32"):
        return "documentation"
    if ip in ipaddress.ip_network("fc00::/7"):
        return "unique-local"
    return "global-unicast"


def main() -> None:
    parser = argparse.ArgumentParser(description="Describe an IPv4 or IPv6 CIDR")
    parser.add_argument("cidr", help="Address with prefix, for example 192.168.56.10/24")
    args = parser.parse_args()
    print(json.dumps(describe_cidr(args.cidr), indent=2))


if __name__ == "__main__":
    main()
