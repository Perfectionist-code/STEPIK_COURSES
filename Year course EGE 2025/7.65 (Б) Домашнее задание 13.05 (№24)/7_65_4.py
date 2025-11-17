with open('04.txt') as file:
    s = file.readline()
print((ls := len(s)))
for char in 'ABCDO':
    if char in 'BCD':
        s= s.replace(char, 'S')
    else:
        s = s.replace(char, 'G')

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if len(c) % 2 == 0:
            if  all(c[i:i+2] == 'SG' for i in range(0, len(c), 2)):
                m = max(m, len(c))
                print(c)
            else:
                break
print(m//2)
