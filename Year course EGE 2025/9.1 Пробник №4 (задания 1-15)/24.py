from re import *

with open('24var01.txt') as file:
    s = file.readline()
print((ls := len(s)))

num = r'(([1-4][0-4]*)|0)'
reg = fr'{num}([\+\-]{num})*'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)
