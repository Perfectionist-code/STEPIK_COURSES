# from re import *
#
# with open('06_24-337.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# reg = r'[1]([0-9|A-D])*[07]'
# reg = fr'(?=({reg}))'
# m = max((x.group(1) for x in finditer(reg, s)), key=len)
# print(len(m), m, int(m, 14) % 7 == 0)


with open('06_24-337.txt') as file:
    s = file.readline()
print((ls := len(s)))

for char in 'EFGHIJKLMNOPQRSTUVWXYZ':
    s = s.replace(char, ' ')

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if c[0] == '1' and ' ' not in c:
            if int(c, 14) % 7 == 0:
                m = max(m, len(c))
                print(c)
        else:
            break
print(m)
