with open('08_k7a-6.txt') as file:
    s = file.readline()
print((l_s := len(s)))
m = 0
for l in range(l_s):
    for r in range(l + m, l_s):
        c = s[l:r + 1]
        if 'A' not in c and 'E' not in c:
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
