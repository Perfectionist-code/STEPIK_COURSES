from re import *

with open('32_24_19970.txt') as file:
    s = file.readline()
print((ls := len(s)))

num = r'([1-9][0-9]*[05]|0)'
reg = fr'{num}([\+\*]{num})*'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)
