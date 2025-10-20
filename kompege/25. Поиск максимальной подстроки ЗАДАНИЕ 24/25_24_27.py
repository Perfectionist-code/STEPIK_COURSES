from re import *

with open('27_24_2428.txt') as file:
    s = file.readline()
print((ls := len(s)))

reg = r'(YZ|Z)?(XYZ)+(XY|X)?'
reg = fr'(?=({reg}))'
res = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(res), res)

