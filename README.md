# Scapy UDP demo 
Author: Matt Weidner @jopawp

This small project demonstrates the ease of implementing a custom application level protocol client using the scapy packet generator. This demo is based on a CTF challenge the author encountered during the National Cyberleague fall 2015 season named "Magic Byte".

## Requirements:
magicbyte.py requires the python3 friendly scapy fork located at: https://github.com/phaethon/scapy

Install with 'python3 setup.py install' from source tree (get it with `git clone https://github.com/phaethon/scapy.git`) or `pip3 install scapy-python3` for latest published version.

Original scapy repository: https://github.com/phaethon/scapy

## server.py
A small UDP server that implements a custom UDP protocol with the following specification:


| Byte 0 |     Byte 1    |           Bytes 2-26           |           Bytes 27-50          |
|:------:|:-------------:|:------------------------------:|:------------------------------:|
|  0x78  |    Unknown    | 23-byte null terminated string | 23-byte null terminated string |

Upon receiving a properly formatted UDP packet with byte 1 set to the "magic" value, a flag is returned.

## magicbyte.py
Client script that brute forces the unknown value using scapy.

See the accompanying blog post at https://mattweidner.github.io/blog/scapy-udp-fuzz-part1.html
