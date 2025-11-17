from itertools import permutations

with open('06.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if all(''.join(per) not in c for per in permutations('QRS', 2)):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
