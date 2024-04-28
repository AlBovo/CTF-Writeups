#!/usr/bin/env python3
from sage.all import *
import re

COEFF = [0] * 101

with open('src.txt') as src:
    for line in src:
        f = re.findall(r'\d+', line)
        if len(f) == 2:
            COEFF[int(f[0])] = int(f[1])

p = 137

for i in range(101):
    COEFF[i] = (i, COEFF[i])
F = GF(p)
R = F['x']
f = R.lagrange_polynomial(COEFF)

for i in range(101, 133):
    print(chr(f(i)), end="")
print()
