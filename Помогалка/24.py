# from re import *
#
# with open('24.txt') as file:
#     s = file.readline()
# print(len(s))
#
# num = r'([1-9][0-9]*|0)'
# reg = fr'(({num}\*)*0(\*{num})*)'
# reg = fr'{reg}(\+{reg})*'
# reg = fr'(?=({reg}))'
# m = max([x.group(1) for x in finditer(reg, s)], key=len)
# print(len(m), m)



from re import *

with open('24.txt') as file:
    s = file.readline()
print(len(s))

num = r'([1-9][0-9]*|0)'
reg = fr'{num}([\+\*]{num})*'
reg = fr'(?=({reg}))'
m = tuple(x.group(1) for x in finditer(reg, s))
m = tuple(x for x in m if eval(x) == 0)
m = max(m, key=len)
print(len(m), m)

