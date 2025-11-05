from fnmatch import fnmatch

mask = '1?2139*4'

for i in range(0, 10 ** 10 + 1, 2023):
    n = str(i)
    if fnmatch(n, mask) and not i % 2023:
        print(i, i // 2023)
