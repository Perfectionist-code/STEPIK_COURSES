# with open('05.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# s = s.replace('O', 'A').replace('D', 'C').replace('F', 'C')
#
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if len(c) % 2 == 0:
#             if all(c[i:i + 2] == 'CA' for i in range(0, len(c), 2)):
#                 m = max(m, len(c))
#                 print(c)
#             else:
#                 break
# print(m // 2)

from re import *

with open('05.txt') as file:
    s = file.readline()
print((ls := len(s)))

reg = r'(CA|DA|FA|CO|DO|FO)+'
reg = fr'(?=({reg}))'
print(len(max((x.group(1) for x in finditer(reg, s)), key=len)) // 2)
