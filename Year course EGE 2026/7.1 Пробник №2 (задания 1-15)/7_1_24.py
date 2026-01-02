with open('24.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if c.startswith('S') and c.count('S') == 1:
            if (sm := sum(c.count(x) for x in ('13579'))) <= 35:
                if sm == 35:
                    m = max(m, len(c))
                    print(c)
            else:
                break
        else:
            break
print(m)
