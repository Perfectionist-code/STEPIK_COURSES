with open('21_24_12476.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if 'ORO' not in c and 'ROR' not in c:
            if c.count('RO') <= 21:
                m = max(m, len(c))
                print(c)
            else:
                break
        else:
            break
print(m)
