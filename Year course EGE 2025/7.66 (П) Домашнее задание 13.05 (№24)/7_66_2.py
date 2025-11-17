from re import finditer

with open('02.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if 'ORO' not in c and 'ROR' not in c:
            if (cnt := c.count('RO')) <= 21:
                if cnt == 21:
                    m = max(m, len(c))
            else:
                break
        else:
            break
print(m)
