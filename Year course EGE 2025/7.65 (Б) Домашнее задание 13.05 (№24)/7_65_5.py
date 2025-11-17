from string import printable

with open('05.txt') as file:
    s = file.readline()
print((ls := len(s)))
hex = printable[:16].upper()

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if c[0] in hex[1:] and all(x in hex for x in c):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
