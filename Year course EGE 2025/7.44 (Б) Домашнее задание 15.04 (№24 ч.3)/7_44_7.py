with open('07_24_14_1715944482.txt') as file:
    s = file.readline()
print((ls := len(s)))
print('----' * 10)

m = 10000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if c.count('E') >= 240:
            m = min(m, len(c))
        else:
            break
print(m)

