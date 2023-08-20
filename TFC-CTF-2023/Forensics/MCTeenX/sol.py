#!/usr/bin/env python3
import os, re
from subprocess import run
from pwn import xor

REGEX = r'".*?"'

with open("temp_file.sh", "w") as f:
    f.write("#!/bin/bash\n")
    f.close()

command = 'bkcrack -C src.zip -c script.sh -p temp_file.sh'
os.system(command)

keys = "c0b1bc78 c3206dfc e7e5bae1"
command = f"bkcrack -C src.zip  -c script.sh -k {keys} -d d.sh && chmod +x d.sh && ./d.sh"
os.system(command)

file = run(["zsteg","red.png"], capture_output=True).stdout.decode()
data = bytes.fromhex(re.findall(REGEX, file)[1][1:-1])
payload = xor(data, b"TFCCTF{")[0:3]
print(xor(payload * (len(data)//3), data).decode())