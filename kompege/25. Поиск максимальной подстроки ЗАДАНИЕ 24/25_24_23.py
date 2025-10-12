with open('23_24_11954.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 500000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if 'Y' not in c:
            if c.count('X') >= 500:
                m = min(m, len(c))
                print(c)
            else:
                break
        else:
            break
print(m)
