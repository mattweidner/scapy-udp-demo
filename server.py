#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# File: server.py
# Author: Matthew A. Weidner <@jopawp>
# Date: 09/04/2016
# Descr: Offline HackerOne report browser using an offline cache contained
# 		 in a sqlite3 database. Ncurses interface.

import os
import sys
import pdb
import sys
import time
import pprint
import random
import socket

G = '\033[92m' #green
Y = '\033[93m' #yellow
B = '\033[94m' #blue
R = '\033[91m' #red
W = '\033[0m'  #white

def listener(port, magic_byte):
    # listen on a UDP port for a payload
    # if the payload contains the magic_byte value, respond with a flag
    # else ignore the packet
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = ('127.0.0.1', int(port))
    print('Listening on {} {}, magic {}'.format(server_addr[0], server_addr[1], magic_byte))
    sock.bind(server_addr)
    while True:
        data, addr = sock.recvfrom(1024)
        #print(len(data), data[0], data[1])
        if (len(data)) == 50:
            if data[0] == 120:
                if data[1] == magic_byte:
                    bytes_sent = sock.sendto(b'flag{brute_forcin_all_teh_things}', addr)
                    # Grab a new magic value
                    magic_byte = random.getrandbits(8)
                    print('Listening on {} {}, magic {}'.format(server_addr[0], server_addr[1], magic_byte))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} missing operand.".format(sys.argv[0]))
        print("Usage: {} <listen_port>".format(sys.argv[0]))
    else:
        # Grab a random magic 8-bit value
        magic_byte = random.getrandbits(8)
        listener(sys.argv[1], magic_byte)
