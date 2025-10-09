with open('06.txt') as file:
    s = file.readline()
print((l_s := len(s)))

m = 0
for l in range(l_s):
    for r in range(l + m, l_s):
        c = s[l:r + 1]
        if 'ad' not in c and 'da' not in c:
            m = max(m, len(c))
        else:
            break
print(m)
