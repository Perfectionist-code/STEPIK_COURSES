from re import *

with open('07.txt') as file:
    s = file.readline()
print((ls := len(s)))

# num = r'(([1-9]|[A-B])([0-9]|[A-B])*)'
# reg = fr'(?=({num}))'
# m = (x.group(1) for x in finditer(reg, s))
# res = tuple(x for x in m if not int(x, 12) % 2)
# m = max(res, key=len)
# print(len(m), m)

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if c[0] != '0' and all(x in '0123456789AB' for x in c):
            if not int(c, 12) % 2:
                m = max(m, len(c))
                print(c)
        else:
            break
print(m)
