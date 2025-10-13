with open('04.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
res = []
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if (f := c.count('T')) <= 100:
            m = max(m, len(c))
            if f == 100:
                res.append(c)
        else:
            break
print(m)
fl = max(res, key=len)
print(len(fl), fl)
