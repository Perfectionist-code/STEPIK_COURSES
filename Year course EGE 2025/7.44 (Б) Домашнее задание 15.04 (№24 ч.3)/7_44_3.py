with open('03_24-263.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 10000
res = []
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if 30 <= c.count('X'):
            m = min((m, len(c)))
            res.append(c)
            print(c)
        else:
            break
res = [x for x in res if x.count('x') <= 80]

print(m)
mn = min(res, key=len)
print(len(mn), mn)