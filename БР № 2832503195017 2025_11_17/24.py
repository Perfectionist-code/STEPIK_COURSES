with open('24_8480.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if all(x not in c for x in 'AB' if 'C' in c) or all(x not in c for x in 'AC' if 'B' in c) or all(x not in c for x in 'BC' if 'A' in c):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)

