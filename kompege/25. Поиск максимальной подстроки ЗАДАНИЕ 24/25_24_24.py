with open('24_24_9169.txt') as file:
    s = file.readline()
print((ls:=len(s)))

m = 100000
for l in range(ls):
    for r in range(l+m,l, -1):
        c = s[l:r+1]
        if c.count('BAD') + c.count('FAT') == 3:
            m = min(m, len(c))
            print(c)
print('-----'*10)
print(m)
