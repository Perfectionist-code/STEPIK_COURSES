from re import *

with open('02_k7a-1.txt') as file:
    s = file.readline()

reg = r'([ABC]+)'
reg = fr'(?=({reg}))'
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m))
