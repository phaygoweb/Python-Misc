#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST

prefix = b'\xFF\xFF\xFF\xFF\xFF\xFF'

data = \
prefix + b'\xAA\xBB\xCC\xDD\xEE\xFF'*16 + \
prefix + b'\xAA\xBB\xCC\xDD\xEE\xFF'*16 + \
prefix + b'\xAA\xBB\xCC\xDD\xEE\xFF'*16 + \
prefix + b'\xAA\xBB\xCC\xDD\xEE\xFF'*16 + \
prefix + b'\xAA\xBB\xCC\xDD\xEE\xFF'*16 + \
prefix + b'\xAA\xBB\xCC\xDD\xEE\xFF'*16 + \
prefix + b'\xAA\xBB\xCC\xDD\xEE\xFF'*16 + \
prefix + b'\xAA\xBB\xCC\xDD\xEE\xFF'*16 + \
prefix + b'\xAA\xBB\xCC\xDD\xEE\xFF'*16 + \
prefix + b'\xAA\xBB\xCC\xDD\xEE\xFF'*16

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.sendto(data, ('<broadcast>', 9))
sock.close()