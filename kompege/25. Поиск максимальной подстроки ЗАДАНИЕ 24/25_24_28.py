from re import *

with open('28_24_18597.txt') as file:
    s = file.readline()
print((ls := len(s)))

float_num = r'([1-9]{4}\.)([0-9]+)'
reg = fr'{float_num}(\&{float_num})+'
reg = fr'(?=({reg}))'
res = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(res), res)