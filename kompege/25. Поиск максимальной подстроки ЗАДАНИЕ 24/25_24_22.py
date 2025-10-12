with open('22_24_6734.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 10000
res = []
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if c.count('.') >= 7:

            m = min(m, len(c))
            print(c)
            if c.count('.') == 7:
                res.append(c)
        else:
            break
f = min(res, key=len)
print(m)
print(len(f), f)
