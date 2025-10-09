with open('03_k7a-4.txt') as file:
    s = file.readline()
print((ln := len(s)))
m = 0
for l in range(ln):
    for r in range(l + m, ln):
        c = s[l:r + 1]
        if 'D' not in c:
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)