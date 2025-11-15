with open('02_k7a-4.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if 'D' not in c:
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
