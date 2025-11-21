from re import *

with open('08.txt') as file:
    s = file.readline()

num = r'(([1-9][0-9]*)|0)'
reg = fr'({num}([\+\*]{num})*)'
reg = fr'(?=({reg}))'
m = [x.group(1) for x in finditer(reg, s)]
m = max([x for x in m if not x.isdigit() and eval(x) == 0], key=len)
print(len(m), m)
