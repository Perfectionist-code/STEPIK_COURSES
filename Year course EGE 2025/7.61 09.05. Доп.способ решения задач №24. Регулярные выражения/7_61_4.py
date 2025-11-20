from re import *

with open('04.txt') as file:
    s = file.readline()

reg = r'(NPO|PNO)+'
# reg = fr'(?=({reg}))'
m = max([x.group() for x in finditer(reg, s)], key=len)
print(len(m) // 3, m)
