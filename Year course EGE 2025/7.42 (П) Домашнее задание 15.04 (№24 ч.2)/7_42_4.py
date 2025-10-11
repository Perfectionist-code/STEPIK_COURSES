# from re import *
#
# with open('04.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# reg = r'D([ACDFO]+)D'
# reg = fr'(?=({reg}))'
#
# max_l = 0
# for x in finditer(reg, s):
#     d = x.group(1)
#     print(d)

#     if (c := x.group(1)).count('O') <= 2:
#         if len(c) > max_l:
#             max_l = len(c)
#             m = (max_l, c)
#             print(*m)
# print(*m)


with open('04.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if c[0] == 'D' and c.count('O') <= 2:
            if c[-1] == 'D':
                m = max(m, len(c))
                print(c)
        else:
            break
print(m)
