#!/usr/bin/python

import sys
from scapy.all import *

class MagicByte(Packet):
    name = "MagicBytePacket "
    fields_desc = [ XByteField("Check",0x78),
            XByteField("GroupID",0),
            StrNullField("pad", "A"*47) ]

if len(sys.argv) != 3:
    print("%s: missing operand." % sys.argv[0])
    print("Usage: magicbyte.py <ip> <port>")
    sys.exit(1)


p = 0
gid = 0

while not p:
    print(gid)
    # Use a layer 3 raw socket so scapy can talk to lo iface.
    # If you're doing this over a real wire, you won't need the
    # following line.
    conf.L3socket=L3RawSocket
    p = sr1(IP(dst=sys.argv[1])/UDP(sport=55555,dport=int(sys.argv[2]))/MagicByte(GroupID=gid),timeout=0.1,verbose=False)
    if p:
        p.show()

    if gid > 255:
        print("ABORT: Max Check value exceeded!")
        sys.exit(1)

    gid += 1
