from re import *

with open('31_24_19968.txt') as file:
    s = file.readline()
print((ls := len(s)))

num = r'([1-5][0-5]*|0)'
reg = fr'{num}([\+\*]{num})*'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)
