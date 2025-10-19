from re import *

with open('25_24_5171.txt') as file:
    s = file.readline()
print((ls:=len(s)))

reg =r'(CA)+(C)*'
reg = fr'(?=({reg}))'
res = max((x.group(1) for x in finditer(reg, s)), key=len)

print(len(res))
print(res)