# CrazyXOR
CrazyXOR provides an attachment containing source code that calculates the crazy XOR of 7 random numbers from `10^5` to `5*10^5`. It uses one of these numbers randomly to seed the random generator, which will then generate the key used to encrypt the flag.

```python
def crazy_xor(x):
	primes = prime_factors(x)
	res = 0

	for p1 in primes:
		for p2 in primes:
			if p1 <= p2:
				res = res ^ math.lcm(p1, p2) # Least common multiple

	return res
```
Once it's observed that the 7 iterations in the challenge meant to make brute-forcing the seed more complex are actually unnecessary, and that brute-forcing each x passed to the crazy XOR directly is sufficient, one just needs to emulate the various steps and check if decrypting the text yields the flag to complete this challenge as well.

### Challenge Description
> When you are on drugs and mix number theory with xor, you forget to make primes private. (the challenge is created by running python3 so do not use python2 to solve it).