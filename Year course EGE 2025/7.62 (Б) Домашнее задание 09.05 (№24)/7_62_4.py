from re import *

with open('04.txt') as file:
    s = file.readline()

reg = r'([AE][BCD])*'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m) // 2, m)
