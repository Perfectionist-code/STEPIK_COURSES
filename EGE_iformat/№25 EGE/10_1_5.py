from fnmatch import fnmatch
mask1 = '4*5*6'
mask2 = '?74*68?'
divider = 2234
for i in range(divider, int(1e10 + 1), divider):
    if fnmatch(s:=str(i), mask1) and fnmatch(s, mask2):
        print(i, i // divider)



