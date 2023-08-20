#!/usr/bin/env python3
from math import log2, ceil
from random import randint
from sys import setrecursionlimit

inputStr = "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24".split()

class SegmentTree:
    n = 0
    size = 0
    tree = []
    def __init__(self, n):
        self.n = n
        self.size = 1 << ceil(log2(n))
        self.tree = [0] * (2 * self.size)

    def update(self, pos, value):
        pos += self.size
        self.tree[pos] = value
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.tree[pos * 2] + self.tree[(pos * 2) + 1]
            pos //= 2
    
    def get_sum(self, node, nl, nr, ql, qr):
        if ql <= nl and nr <= qr:
            return self.tree[node]
        if nr <= ql or qr <= nl:
            return 0
            
        left = self.get_sum(2 * node, nl, (nl + nr) // 2, ql, qr)
        right = self.get_sum((2 * node) + 1, (nl + nr) // 2 , nr, ql, qr)
        return left + right

    def get_tree(self):
        return self.tree

def normal_writeup():
    flag = [" "] * len(inputStr)
    for i in inputStr:
        c = i[0]
        pos = int(i[1:])
        flag[pos] = c

    print("".join(i for i in flag))

def nice_writeup():
    tree = SegmentTree(len(inputStr))
    sum = 0
    for i in inputStr:
        c = i[0]
        pos = int(i[1:])
        sum += ord(c)
        tree.update(pos, ord(c))
    assert tree.get_sum(1, 0, len(inputStr)-1, 0, len(inputStr)-1) == sum
    l = randint(0, len(inputStr)-2)
    r = randint(l, len(inputStr)-1)
    sum = tree.get_sum(1, 0, len(inputStr)-1, l, r)
    print(f"If the sum of the query will be equals to {sum} you'll get the flag!")
    l, r = int(input("Enter the range [left]: ")), int(input("Enter the range [right]: "))
    if tree.get_sum(1, 0, len(inputStr)-1, l, r) == sum:
        normal_writeup()
    else:
        print("Wrong lol")
        # os.system('rm -rf /')

setrecursionlimit(int(500000000))

if __name__ == "__main__":
    i = input("Enter 1 for normal writeup, 2 for nice writeup: ")
    if i == "1":
        normal_writeup()
    elif i == "2":
        nice_writeup()
    else:
        print("Do you want to pwn me?")
        # os.system("rm -rf /")
    