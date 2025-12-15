with open('24.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if c[0] in '02468' and sum((c.count(x) for x in '02468')) == 1:
            if (cn := c.count('F')) <= 67:
                if cn == 67:
                    m = max(m, len(c))
            else:
                break
        else:
            break
print(m)
