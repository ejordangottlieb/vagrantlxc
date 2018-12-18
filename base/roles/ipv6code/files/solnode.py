#!/usr/bin/env python3

from ipaddress import IPv6Address
from ipaddress import IPv6Network
import sys

def solicit_node(addr):
    solicitnode = IPv6Network("FF02:0:0:0:0:1:FF00::/104")
    sixaddr = IPv6Address(addr)
    x = int(sixaddr) & 0xffffff
    mac = x + 0x3333ff000000
    return ( "{}:{}:{}:{}:{}:{}".format(hex(mac)[2:][0:2],
                                        hex(mac)[2:][2:4],
                                        hex(mac)[2:][4:6],
                                        hex(mac)[2:][6:8],
                                        hex(mac)[2:][8:10],
                                        hex(mac)[2:][10:12]),
             "{}".format(solicitnode[x]))


print(solicit_node(sys.argv[1]))
