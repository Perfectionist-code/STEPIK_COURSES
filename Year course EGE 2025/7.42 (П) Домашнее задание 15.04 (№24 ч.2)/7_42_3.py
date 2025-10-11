# from re import *
#
# with open('03.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# comb = r'[ZX]Y'
# reg = fr'({comb})+'
# reg = fr'(?=({reg}))'
# m = [x.group(1) for x in finditer(reg, s)]
# m = [x for x in m if 'XYZY' not in x]
# m = max(m, key=len)
# print(len(m) // 2, m)

with open('03.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if len(c) % 2 == 0:
            if all((c[i:i + 2] in ('XY', 'ZY') for i in range(0, len(c), 2))) and 'XYZY' not in c:
                m = max(m, len(c))
                print(c)
            else:
                break
        # else:
        #     break
print(m // 2)
