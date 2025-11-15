with open('04.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if 'ad' not in c and 'da' not in c:
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
