with open('02.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if len(c) % 3 == 0:
            if all((c[i:i+3] in ('NPO', 'PNO') for i in range(0, len(c), 3))):
                m = max(m, len(c))
            else:
                break
        else:
            continue
print(m // 3)
