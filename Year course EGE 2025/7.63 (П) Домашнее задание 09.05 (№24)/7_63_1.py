from re import *

with open('01.txt') as file:
    s = file.readline()

num = r'(([6789]([06789])*)|0)'
reg = fr'{num}([\*\-]{num})*'
reg = fr'(?=({reg}))'
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m), m)
print(eval(m))
