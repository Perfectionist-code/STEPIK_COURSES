with open('08.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if 'QW' not in c:
            m = max(m, len(c))
        else:
            break
print(m)

