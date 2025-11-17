from fnmatch import fnmatch

mask = '2?34?56?8'

for n in range(0, 10**9 +1, 151):
    if fnmatch(str(n), mask):
        print(n, n // 151)