with open('01_24-181.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if c.count('.') <= 5:
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
