with open('09.txt') as file:
    s = file.readline()
print((ls := len(s)))
for char in 'GHIJKLMNOPQRSTUVWXYZ':
    s = s.replace(char, ' ')

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if c[0] != '0' and ' ' not in c:
            if set(c) <= set('0123456789ABCDEF'):
                m = max(m, len(c))
                print(c)
        else:
            break
print(m)
