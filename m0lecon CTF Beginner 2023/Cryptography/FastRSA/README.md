# Fast RSA
This time, the challenge requires decrypting the flag encrypted in RSA where `p - q = 4`. This, of course, is very vulnerable because if `p equals q` then it's easy to calculate the square root of the modulus N and then look for a value such that `N mod v = 0`. At this point, `v` will be `p` and `q` will be calculated by dividing the modulus by `q`. The problem can be then solved by calculating the key `d`.

### Challenge description
>I have found a new way to generate my RSA primes but i think i messed up something