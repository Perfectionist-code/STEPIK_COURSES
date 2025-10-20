from re import *

with open('29_24_19969.txt') as file:
    s = file.readline()
print((ls := len(s)))

reg = r'([a-z]+)@([a-z]+)\.([a-z]+)'
reg = fr'(?=({reg}))'
res = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(res), res)


