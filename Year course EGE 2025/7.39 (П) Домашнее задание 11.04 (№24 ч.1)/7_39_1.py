with open('01_24-181.txt') as file:
    s = file.readline()
print((l_s := len(s)))

m = 0
for l in range(l_s):
    for r in range(l + m, l_s):
        c = s[l:r + 1]
        if c.count('.') <= 1:
            m = max(m, len(c))
            # print(c)
        else:
            break
print(m)
