#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt
from pwn import *
import gmpy2

r = remote('third-times-the-charm.ctf.umasscybersec.org', 1337)
f = False
m = [0] * 3
N = [0] * 3

for i in range(7):
    r.recvuntil(b': ')
    try:
        d = int(r.recvline().decode().strip())
        if f:
            N[(i - 1) // 2] = d
        else:
            m[(i - 1) // 2] = d
        f = not f
    except:
        pass

n = crt(N, m)[0]
with gmpy2.local_context(gmpy2.context(), precision=800) as ctx:
    root = gmpy2.cbrt(n)

print(long_to_bytes(int(root)).decode())