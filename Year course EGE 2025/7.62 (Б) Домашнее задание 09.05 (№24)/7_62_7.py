from re import *

with open('07.txt') as file:
    s = file.readline()

reg = r'(CFE|FCE)+'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m) // 3, m)
