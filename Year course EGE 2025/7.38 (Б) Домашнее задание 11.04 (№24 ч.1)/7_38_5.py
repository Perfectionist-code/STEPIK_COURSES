with open('05.txt') as file:
    s = file.readline()
print((ls := len(s)))
print('----' * 5)

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if all(c[i] != c[i + 1] for i in range(len(c) - 1)):
            m = max(m, len(c))
            print(c)
        else:
            break
print('----' * 5)
print(m)
