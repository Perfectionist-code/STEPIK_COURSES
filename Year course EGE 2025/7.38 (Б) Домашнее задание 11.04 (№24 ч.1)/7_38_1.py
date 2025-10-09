with open('01_k7a-2.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if all(x not in c for x in 'BEF'):
            m = max(m, len(c))
            print(c)
print(m)
