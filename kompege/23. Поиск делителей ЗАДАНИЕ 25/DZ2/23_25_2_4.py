from fnmatch import fnmatch

mask = '12*45*'

for i in range(0, 10 ** 6 + 1, 51):
    n = str(i)
    if fnmatch(n, mask) and not i % 51:
        print(i, i // 51)
