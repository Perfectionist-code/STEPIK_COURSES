with open('01_k7.txt') as file:
    s = file.readline()
print(len(s))

m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if all(char == 'C' for char in c):
            m = max(m, len(c))
        else:
            break
print(m)
