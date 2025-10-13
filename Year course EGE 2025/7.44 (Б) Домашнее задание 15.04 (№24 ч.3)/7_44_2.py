with open('02_24-263.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 10000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if c.count('A') >= 30:
            m = min(m, len(c))
            print(c)
        else:
            break
print(m)
