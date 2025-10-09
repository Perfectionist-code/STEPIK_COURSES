with open('05_24-j7.txt') as file:
    s = file.readline()
for char in ('2468'):
    s = s.replace(char, '0')
for char in ('13579'):
    s = s.replace(char, '1')
print((l_s := len(s)))

m = 0
for l in range(l_s):
    for r in range(l + m, l_s):
        c = s[l:r + 1]
        if len(set(c)) == 1:
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
