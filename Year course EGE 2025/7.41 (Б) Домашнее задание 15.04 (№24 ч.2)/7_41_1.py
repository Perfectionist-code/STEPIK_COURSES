from re import *

with open('01.txt') as file:
    s = file.readline()
print((ls := len(s)))
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if len(c) % 2 == 0:
#             if all(c[i:i + 2] in ('BA', 'DA') for i in range(0, len(c), 2)):
#                 m = max(m, len(c))
#                 print(c)
#             else:
#                 break
# print(m//2)

reg = r'(BA|DA)+'
reg = rf'(?=({reg}))'

print(max(len(x.group(1)) for x in finditer(reg,s))//2)
