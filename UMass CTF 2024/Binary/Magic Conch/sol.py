#!/usr/bin/env python3
from pwn import *
import re

r = remote('magic-conch.ctf.umasscybersec.org', 1337)
PAYLOAD = 'A' * 16 + 'B' * 16

r.recvuntil(b': ')
r.sendline(PAYLOAD.encode())
r.recvuntil(b': ')
r.sendline(PAYLOAD.encode()[::-1])

resp = r.recvuntil(b'}').decode()
print(re.findall(r'UMASS\{.*\}', resp)[0])