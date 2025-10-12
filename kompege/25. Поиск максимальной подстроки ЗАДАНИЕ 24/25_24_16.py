from re import *

with open('16_24_9552.txt') as file:
    s = file.readline()
print((ls := len(s)))

reg = r'(PC|CSGO)+'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)

