#!/usr/bin/env python3
import PIL, re
from PIL import Image

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
I used wireshark to find the photo in the 10th packet. 
I then extracted it and i used this script to get the flag. 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

REGEX = r"TFCCTF{.*?}"

im = Image.open("photo.png")
x, y = im.size

data = []

for i in [0, 4, 8]: # the three pixel lines
    for e in range(y):
        if im.getpixel((i, e)) == (0, 0, 0): # black pixel
            break
        data.append(list(im.getpixel((i, e)))[1])

"""
for i in data:
    print(chr(i), end="")
"""

data = ''.join(chr(i) for i in data)
flag = re.findall(REGEX, data)[0]
print(flag)