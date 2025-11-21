from re import *

with open('10.txt') as file:
    s = file.readline()

reg = r'(FE)*F{0,1}'
reg = fr'(?=({reg}))'
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m), m)

reg = r'(EF)*E{0,1}'
reg = fr'(?=({reg}))'
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m), m)