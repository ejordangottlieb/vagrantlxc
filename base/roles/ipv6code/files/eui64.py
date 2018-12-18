#!/usr/bin/env python3

from ipaddress import IPv6Network
from re import split

# Take MAC address and IPv6 prefix
# Assumes MAC address is in xx:xx:xx:xx:xx:xx form
def eui_ipsix(mac,prefix):
    # Extract each MAC address octet into list
    octet = split(":", mac)
    # Flip bit 7 of high order 8 bits of MAC address
    octet[0] = hex( int(octet[0],16) ^ 2)[2:]
    # Insert ffee between high order 24-bits and rest of MAC address and convert
    # to integer
    eui64 = int("{}fffe{}".format(''.join(octet[:3]),''.join(octet[3:6])),16)
    # Create IPv6 prefix object
    prefixsix = IPv6Network(prefix)
    # Return IPv6 address using eui64 integer value index of IPv6 prefix object
    return prefixsix[eui64]

print(eui_ipsix("ba:93:73:ef:6d:ee","fe80::/10"))
