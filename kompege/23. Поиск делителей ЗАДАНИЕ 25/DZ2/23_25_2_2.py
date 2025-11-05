from fnmatch import fnmatch

mask = '1234*7'

for i in range(123400, 10 ** 8 + 1):
    n = str(i)
    if fnmatch(n, mask) and not i % 141:
        print(i, i // 141)
