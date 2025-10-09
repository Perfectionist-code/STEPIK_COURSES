with open('03.txt') as file:
    s = file.readline().replace('2', '1').replace('3', '1')
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if set(c) == {'1'}:
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
