with open('06.txt') as file:
    s = file.readline()
print((ls := len(s)))
print('----' * 10)

m = 0
res = []
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if (fl := c.count('AB')) <= 50:
            m = max(m, len(c))
        if fl == 50:
            res.append(c)
        else:
            break
print(m)
fl = max(res, key=len)
print(len(fl), fl)
