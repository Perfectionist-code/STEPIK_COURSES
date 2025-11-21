from re import *

with open('09_zadanie24_2.txt') as file:
    s = file.readline()

reg = r'(LDR)+(LD|L){0,1}'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)
