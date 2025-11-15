from re import finditer

with open('05.txt') as file:
    s = file.readline()
print((ls := len(s)))

# reg = r'(AB|AC)+'
# reg = fr'(?=({reg}))'
# res = max([x.group(1) for x in finditer(reg,s)], key=len)
# print(len(res), res)

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if len(c) % 2 == 0:
            if all([c[i:i + 2] in ('AB', 'AC') for i in range(0, len(c), 2)]):
                m = max(m, len(c))
                print(c)
            else:
                break
print(m // 2)
