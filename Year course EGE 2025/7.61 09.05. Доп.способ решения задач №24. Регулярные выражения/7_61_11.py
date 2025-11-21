from re import *

with open('11.txt') as file:
    s = file.readline()

reg = r'[^GWP]*'
reg = fr'(?=({reg}))'
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m), m)
