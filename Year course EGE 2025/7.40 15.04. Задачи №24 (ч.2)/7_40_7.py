with open('07.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if c[0] != '0':
            if all(x in '0123456789AB' for x in c) and c[-1] in '02468A':
                m = max(m, len(c))
                print(c)
            else:
                break
        else:
            break
        if l % 100000 == 0: print(l, ls, m)
print(m)

