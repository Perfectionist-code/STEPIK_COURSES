from re import *

with open('01_24-337.txt') as file:
    s = file.readline()
print((ls := len(s)))

num = r'[1-9]([0-9|A-D])*[7|0]0'
reg = fr'(?=({num}))'
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m), m)


# with open('01_24-337.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
# for char in 'EFGHIJKLMNOPQRSTUVWXYZ':
#     s = s.replace(char, ' ')
#
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if c[0] != '0' and ' ' not in c:
#             if int(c, 14) % 98 == 0:
#                 m = max(m, len(c))
#                 print(c)
#         else:
#             break
# print(m)
