with open('09.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if 'PR' not in c and 'RP' not in c:
            m = max(m, len(c))
        else:
            break
print(m)