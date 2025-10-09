with open('05_24-280.txt') as file:
    s = file.readline()
print((l_s := len(s)))

m = 0
for l in range(l_s):
    for r in range(l + m, l_s):
        c = s[l:r + 1]
        if len(c) == len(set(c)):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
