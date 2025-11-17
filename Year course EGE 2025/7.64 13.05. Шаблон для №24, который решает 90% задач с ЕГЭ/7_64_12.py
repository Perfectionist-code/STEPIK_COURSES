from string import ascii_uppercase

with open('12.txt') as file:
    s = file.readline()
print((ls := len(s)))
for char in 'AEIOUY':
    s = s.replace(char, '*')
for char in ascii_uppercase:
    s = s.replace(char, '#')

m = 10000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if c.count('##*') >= 500:
            m = min(m, len(c))
        else:
            break
print(m)
