from re import *

with open('05.txt') as file:
    s = file.readline()

reg = r'(SQ|Q){0,1}(RSQ)+(RS|R){0,1}'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)
