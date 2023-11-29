# AND Cipher
This challenge required decrypting a cipher that used the bitwise AND operation. Obviously, this operation is not reversible, so one way to solve this problem is to make several requests to the API endpoint to obtain the encrypted flag each time with a different key.

At this point, it's necessary to save the maximum value of the bytes for each position, and if a good bound is chosen, the flag will be found.

```python
for _ in range(250):
    json = requests.get(URL + "api/encrypt").json()
    json = bytes.fromhex(json['encrypted'])
    for i in range(26):
        flag[i] = max(flag[i], json[i])
```

### Challenge Description
> The XOR is so boring... Let's try something different: the AND cipher! <br>
> I wrote the encryption function, but I'm not able to write the decryption function. Can you help me?