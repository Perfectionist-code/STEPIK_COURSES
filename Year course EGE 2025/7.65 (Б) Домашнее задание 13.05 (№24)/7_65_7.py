from string import printable

with open('07.txt') as file:
    s = file.readline()
print((ls := len(s)))

ch = printable[:14].upper()
m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if c[0] in ch[1:] and all(x in ch for x in c):
            if int(c, 14) % 2 ==0:
                m = max(m, len(c))
                print(c)
        else:
            break
print(m)


# from re import *
#
# with open('07.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# num = r'[1-9|A-D]([0-9|A-D])*[02468]'
# reg = fr'(?=({num}))'
# m = max([x.group(1) for x in finditer(reg, s)], key=len)
# print(len(m), m)
