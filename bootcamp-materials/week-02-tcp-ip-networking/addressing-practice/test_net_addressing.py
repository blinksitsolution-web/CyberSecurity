import pytest

from net_addressing import classify_ipv6, describe_cidr, same_subnet


def test_ipv4_lab_subnet():
    info = describe_cidr("192.168.56.10/24")
    assert info["version"] == 4
    assert info["network"] == "192.168.56.0"
    assert info["netmask"] == "255.255.255.0"
    assert info["broadcast"] == "192.168.56.255"
    assert info["usable_hosts"] == 254


def test_same_subnet_matches_lab_hosts():
    assert same_subnet("192.168.56.10", "192.168.56.20", 24)
    assert not same_subnet("192.168.56.10", "10.0.0.5", 24)


def test_ipv6_types():
    assert classify_ipv6("::1") == "loopback"
    assert classify_ipv6("fe80::1") == "link-local"
    assert classify_ipv6("ff02::1") == "multicast"
    assert classify_ipv6("2001:db8::5") == "documentation"
    assert classify_ipv6("fd12:3456::1") == "unique-local"


def test_ipv6_description_has_no_broadcast():
    info = describe_cidr("2001:db8::10/64")
    assert info["version"] == 6
    assert info["network"] == "2001:db8::"
    assert "broadcast" not in info


def test_classify_rejects_ipv4():
    with pytest.raises(ValueError):
        classify_ipv6("192.168.56.10")
