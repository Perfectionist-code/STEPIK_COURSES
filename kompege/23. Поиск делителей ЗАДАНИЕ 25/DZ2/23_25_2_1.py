from fnmatch import fnmatch

cnt = 0
res = []
masks = ('*0??3*', '*4??2', '*1*')
for n in range(700001, 1000000):
    if not n % 13 and not any((fnmatch(str(n), mask) for mask in masks)):
        res.append((n, sum(int(x) for x in str(n))))
        cnt += 1
    if cnt == 5:
        break
for tp in res:
    print(*tp)
