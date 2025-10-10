from itertools import product

with open('06.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if all(''.join(pr) not in c for pr in set(product('XYZ', repeat=2))):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
