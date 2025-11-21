from re import *

with open('09.txt') as file:
    s = file.readline()

num = r'(([7-9][0789]*))'
reg = fr'({num}([\-\*]{num})*)'
reg = fr'(?=({reg}))'
m = max([x.group(1) for x in finditer(reg, s)], key=len)

print(len(m), m)
