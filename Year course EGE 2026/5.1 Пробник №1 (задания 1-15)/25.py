from fnmatch import fnmatch

mask = '7?2*4??9?'

for n in range(0, 10 ** 10 + 1, 96437):
    if fnmatch(str(n), mask):
        print(n, n // 96437)
