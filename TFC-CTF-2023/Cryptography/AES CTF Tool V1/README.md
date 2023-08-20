# AES CTF Tool V1
This challenge was pretty easy because the only thing that had to be done was to download and install the tool given by the admins of the CTF.<br>
You could install it by doing this command:
```git clone https://github.com/hofill/AES-CTF-Tool.git && cd AES-CTF-Tool && pip install -r requirements.txt```<br>Then you had to change the `main.py` file by changing the function `init_server` <br>from this `return process(["./test_servers/ecb.py"])`<br> to this `return remote("challs.tfcctf.com", 31737)` (obviusly by also changing the port).<br><br>
This was part of the result:<br>
<image src="example.png" name="example">