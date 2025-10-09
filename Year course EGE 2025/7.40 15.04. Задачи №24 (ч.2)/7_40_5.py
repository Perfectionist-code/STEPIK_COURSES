with open('05.txt') as file:
    s = file.readline()
    for char in 'QRS':
        s = s.replace(char, '*')
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if all(c[i:i + 2] != '**' for i in range(len(c) - 1)):
            m =max(m, len(c))
            # print(c)
        else:
            break
print(m)
