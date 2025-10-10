with open('07_24_4627.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if len(c) % 3 == 0:
            if all(c[i:i + 3] in ('NPO', 'PNO') for i in range(0, len(c), 3)):
                m = max(m, len(c))
                print(c)
            else:
                break
print(m // 3)

# from re import *
#
# with open('07_24_4627.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# reg = r'(NPO|PNO)+'
# reg = fr'(?=({reg}))'
# print(len(max((x.group(1) for x in finditer(reg, s)), key=len)) // 3)
