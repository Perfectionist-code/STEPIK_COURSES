with open('08_24-337.txt') as file:
    s = file.readline()
print((ls := len(s)))
for c in 'GHIJKLMNOPQRSTUVWXYZ':
    s =  s.replace(c, ' ')
m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if c[0] == '8' and ' ' not in c:
            if c[-1] in '08':
                m = max(m, len(c))
                print(c)
            # else:
            #     break
        else:
            break
    # if l % 100000 == 0: print(l, ls, m)
print(m)