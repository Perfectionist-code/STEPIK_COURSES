with open('09_24_4643.txt') as file:
    s = file.readline()
print((ls := len(s)))

s = s.replace('B', 'A').replace('2', '1')

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if len(c) % 3 == 0:
            if all((c[i:i + 3] == '11A' for i in range(0, len(c), 3))):
                m = max(m, len(c))
                print(c)
            else:
                break
print(m // 3)