#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: echo_server.py
# Author: Matthew A. Weidner <@jopawp>
# Publication Date: 09/04/2016
# Descr: Listens on an arbitrary UDP port, specified on the command line,
#        and echos back the data it receives.
#

import sys
import socket

def listener(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_addr = ('127.0.0.1', int(port))
	print('Listening on {} {}'.format(server_addr[0], server_addr[1]))
	sock.bind(server_addr)
	while True:
		data, addr = sock.recvfrom(1024)
		bytes_sent = sock.sendto(data, addr)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('{} missing operand.'.format(sys.argv[0]))
		print('Usage: {} <listen_port>'.format(sys.argv[0]))
	else:
		listener(sys.argv[1])
