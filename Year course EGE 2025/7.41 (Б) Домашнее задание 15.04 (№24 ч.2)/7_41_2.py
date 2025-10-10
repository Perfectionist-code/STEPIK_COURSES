def cond(para, c1: str) -> bool:
    return all(c1[i:i + 2] in para for i in range(0, len(c1), 2))


with open('02.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if len(c) % 2 == 0:
            if cond(('AC', 'AB'), c):
                m = max(m, len(c))
                print(c)
            else:
                break
print(m // 2)


# from re import *
#
#
# with open('02.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
#
# reg = r'(AB|AC)+'
# reg = fr'(?=({reg}))'
# print(len(max((x.group(1) for x in finditer(reg, s)), key=len)) // 2)
