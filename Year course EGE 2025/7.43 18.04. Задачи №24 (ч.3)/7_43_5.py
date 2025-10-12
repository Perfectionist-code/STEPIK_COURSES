with open('05_24var08.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l+m, ls):
        c = s[l:r+1]
        if c.count('AB') <= 21:
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)


