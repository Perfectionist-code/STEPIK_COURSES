from fnmatch import fnmatch
mask = '?46?44*2'
divider = 6718
for i in range(divider, int(1e9 + 1), divider):
    if fnmatch(str(i), mask):
        print(i, i // divider)