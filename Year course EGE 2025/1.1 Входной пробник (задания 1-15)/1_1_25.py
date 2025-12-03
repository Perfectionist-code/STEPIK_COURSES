from fnmatch import fnmatch

mask = '9*?001?1'

for n in range(0, 10 ** 10 + 1, 12007):
    if fnmatch(str(n), mask):
        print(n, n // 12007)
