from string import ascii_uppercase

with open('11.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 10000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if all(x in c for x in ascii_uppercase):
            m = min(m, len(c))
            print(m)
        else:
            break
print(m)
