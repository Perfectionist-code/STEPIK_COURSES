from fnmatch import fnmatch

mask = '12345?6?8'

for i in range(100000000, 10 ** 9 + 1):
    n = str(i)
    if fnmatch(n, mask) and not i % 17:
        print(i, i // 17)
