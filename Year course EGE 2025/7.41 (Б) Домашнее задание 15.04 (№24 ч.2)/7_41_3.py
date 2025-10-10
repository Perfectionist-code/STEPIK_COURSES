with open('03.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if len(c) % 3 == 0:
            if all(c[i:i + 3] in ('ZXY', 'ZYX') for i in range(0, len(c), 3)):
                m = max(m, len(c))
                print(c)
            else:
                break
print(m // 3)


# from re import *
# with open('03.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# reg = r'(ZXY|ZYX)+'
# reg = fr'(?=({reg}))'
# print(len(max([x.group(1) for x in finditer(reg, s)], key=len))//3)

