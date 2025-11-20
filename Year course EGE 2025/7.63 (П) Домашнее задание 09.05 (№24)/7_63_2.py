from re import *

with open('02.txt') as file:
    s = file.readline()

num = r'(([1-9][0-9]*[05])|[05])'
reg = fr'({num}([\+\*]{num})*)'
reg = fr'(?=({reg}))'
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m), m)
