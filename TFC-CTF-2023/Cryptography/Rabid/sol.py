#!/usr/bin/env python3
from base64 import b64decode

input = "VEZDQ1RGe13kwdV9yNGIxZF9kMGc/IT8hPyE/IT8hPi8+Pz4/PjEyMzkwamNhcHNrZGowOTFyYW5kb21sZXR0ZXJzYW5kbnVtYmVyc3JlZWVlMmozfQ=="
flag = b64decode(input)[:len('TFCCTF{')] + b64decode(input[1:])[len('TFCCTF{'):]
print(flag.decode())