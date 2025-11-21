from re import *

with open('08.txt') as file:
    s = file.readline()

reg = r'(YZ|Z){0,1}(XYZ)+(XY|X){0,1}'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)
