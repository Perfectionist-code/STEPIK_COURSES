from re import *
from string import ascii_uppercase

with open('24_324.txt') as file:
    s = file.readline()
print((ls := len(s)))

# reg = r'([A-Z]*)'
# reg = fr'(?=({reg}))'
# res = max([x.group(1) for x in finditer(s, reg)], key=len)
# print(len(res), res)

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if all(x in ascii_uppercase for x in c):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
