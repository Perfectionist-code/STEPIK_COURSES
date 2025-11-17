with open('11_24-296.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 10000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if c.count('AF') > 200:
            m = min(m, len(c))
            print(c)
        else:
            break
print(m)

# for i, h in enumerate([int(input()) for _ in range(int(input()))], 1):
#     if h <= 437:
#         print(f'Crash {i}')
#         break
# else:
#     print('No crash')
