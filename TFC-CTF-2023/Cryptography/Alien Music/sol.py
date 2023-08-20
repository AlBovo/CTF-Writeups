#!/usr/bin/env python3

text = "DC# C#D# C#C C#C DC# C#D# E2 C#5 CA EC# CC DE CA EB EC# D#F EF# D6 D#4 CC EC EC CC# D#E CC E4".split()

d = {
    "A#" : "1", "C#" : "4", "D#" : "6", "F#" : "9", "A": "0",
    "B" : "2", "C" : "3", "D": "5", "E" : "7", "F" : "8",
    "1": "a", "2" : "b", "3" : "c", "4" : "d", "5" : "e", "6" : "f"
}

flag = ''

for i in text:
    t, temp = [""]*2, i
    for e in list(d.keys()):
        if e in temp:
            t[0 if temp.find(e) == 0 else 1] = d[e]
            temp = temp.replace(e, " ")
    flag += chr(int("".join(i for i in t), 16))
print(flag)