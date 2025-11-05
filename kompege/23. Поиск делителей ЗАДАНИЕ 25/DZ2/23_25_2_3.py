from fnmatch import fnmatch

mask = '123*567?'

for i in range(0, 10 ** 9 + 1, 169):
    n = str(i)
    if fnmatch(n, mask) and not i % 169:
        print(i, i // 169)
