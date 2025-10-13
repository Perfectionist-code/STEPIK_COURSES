with open('08.txt') as file:
    s = file.readline()
print((ls := len(s)))
print('----' * 10)

m = 0
res = []
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if (fl := c.count('CD')) <= 160:
            m = max(m, len(c))
            # print(c)
            if fl == 160:
                res.append(c)
        else:
            break
    if l % 100000 == 0:
        print(l, ls, m)
print(m)
fl = max(res, key=len)
print(len(fl), fl)
