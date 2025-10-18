from re import *

reg = r'( .а.а.а[ .,?!-])'
res = []
with open('15_10_5363.txt', 'r', encoding='UTF-8') as file:
    for s in file:
        find = [x.group() for x in finditer(reg,s.strip())]
        res.extend(find)
print(res)
print(len(res))


