with open('24_2_1733757953.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if all(c.count(x) == 1 for x in c):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
