# with open('15_24_4113.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if len(c) % 2 == 0:
#             if ('A' not in c) and all((c[i:i + 2] in ('BB', 'DD') for i in range(0, len(c), 2))):
#                 m = max(m, len(c))
#                 print(c)
#             else:
#                 break
# print(m // 2)


from re import *

with open('15_24_4113.txt') as file:
    s = file.readline()
print((ls := len(s)))

reg = r'(BB|DD)+'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m) // 2, m)
