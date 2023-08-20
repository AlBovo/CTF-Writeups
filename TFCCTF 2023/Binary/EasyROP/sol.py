#!/usr/bin/env python3
from pwn import *

if args.REMOTE:
    p = remote('challs.tfcctf.com', int(input("Port: ")))
else:
    p = process('./src')
