#!/usr/bin/env python3

from ipaddress import IPv6Address
import sys

def mcast_mac(address):
    sixmcast = IPv6Address(address)
    x = int(sixmcast) & 0xffffffff
    mac = x + 0x333300000000
    return ( "{}:{}:{}:{}:{}:{}".format(hex(mac)[2:][0:2],
                                        hex(mac)[2:][2:4],
                                        hex(mac)[2:][4:6],
                                        hex(mac)[2:][6:8],
                                        hex(mac)[2:][8:10],
                                        hex(mac)[2:][10:12]))

print(mcast_mac(sys.argv[1]))
