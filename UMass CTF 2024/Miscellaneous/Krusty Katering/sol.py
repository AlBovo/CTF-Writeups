#!/usr/bin/env python3
from pwn import *
import re

r = remote('krusty-katering.ctf.umasscybersec.org', 1337)

def parse_time_string(time_string):
    minutes, seconds = [0] * 2
    match = re.match(r"(\d+)m", time_string)
    if match:
        minutes = int(match.group(1))
    match = re.search(r"(\d+)s", time_string)
    if match:
        seconds = int(match.group(1))
    
    return minutes, seconds

for i in range(7):
    t = [0] * 10
    for i in range(1000):
        r.recvuntil(b'cook: ')
        time = parse_time_string(r.recvline().strip().decode())
        time = time[0] * 60 + time[1]
        print((i+1), time)
        minim = t.index(min(t))
        t[minim] += time
        print(t)
        r.recvuntil(b'[1-10]\n')
        r.sendline(str(minim + 1).encode())
    print(r.recv(50).strip().decode())
r.interactive()
