with open('04.txt') as file:
    s = file.readline()
print((ln := len(s)))

m = 0
for l in range(ln):
    for r in range(l + m, ln):
        c = s[l: r + 1]
        if all(c[i] != c[i + 1] for i in range(len(c) - 1)):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
