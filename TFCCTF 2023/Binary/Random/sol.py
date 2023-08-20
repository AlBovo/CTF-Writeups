#!/usr/bin/env python3
import random
from pwn import *
from ctypes import CDLL
from time import time

if args.REMOTE:
    p = remote('challs.tfcctf.com', int(input("Port: ")))
else:
    p = process('./src')

libc = CDLL('libc.so.6')
t = int(time())
libc.srandom(t)
p.recvuntil(b'\n')
for i in range(10):
    p.sendline(str(libc.rand()).encode())
p.interactive()