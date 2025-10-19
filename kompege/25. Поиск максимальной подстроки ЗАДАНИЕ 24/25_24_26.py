from re import *

with open('26_24_2425.txt') as file:
    s = file.readline()
print((ls := len(s)))

reg = r'(DBAC)+(DBA|DB|D)*'
reg = fr'(?=({reg}))'
res = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(res), res)
