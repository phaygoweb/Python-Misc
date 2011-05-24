#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST

prefix = b'\xFF\xFF\xFF\xFF\xFF\xFF'

data = \
prefix + b'\xD8\xD3\x85\x80\xF0\x26'*16 + \
prefix + b'\xD8\xD3\x85\x81\x6A\xAC'*16 + \
prefix + b'\xD8\xD3\x85\x81\x6A\x82'*16 + \
prefix + b'\xD8\xD3\x85\x81\x6A\x74'*16 + \
prefix + b'\x78\xE7\xD1\x7F\x06\xB0'*16 + \
prefix + b'\x78\xE7\xD1\x7F\x06\x81'*16 + \
prefix + b'\xD8\xD3\x85\x81\x6A\x93'*16 + \
prefix + b'\x78\xE7\xD1\x7F\x06\x84'*16 + \
prefix + b'\xD8\xD3\x85\x81\x6A\x7A'*16 + \
prefix + b'\xD8\xD3\x85\x81\x6A\xA5'*16

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.sendto(data, ('<broadcast>', 9))
sock.close()