from re import *

with open('06.txt') as file:
    s = file.readline()

reg = r'([1-9|A-F]*)'
reg = fr'(?=({reg}))'
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m), m)
