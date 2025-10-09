with open('03.txt') as file:
    s = file.readline()
print((l_s := len(s)))

m = 0
for l in range(l_s):
    for r in range(l + m, l_s):
        c = s[l:r + 1]
        if all(c[i] <= c[i + 1] for i in range(len(c) - 1)):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
