#!/usr/bin/env python3
import pyshark, re
from base64 import b64decode

cap = pyshark.FileCapture('list.pcap', display_filter='http.request.method == "POST" && frame.len == 756')
flag = ""
REGEX = r'".*?="'
REGEXCHAR = r'\".*\"'

for i in cap:
    base = re.findall(REGEX, i["URLENCODED-FORM"].value)[0][1:-1]
    char = b64decode(base).decode()
    # print(char)
    flag += str(re.findall(REGEXCHAR, char)[0]).replace('"',"")
    print(flag)