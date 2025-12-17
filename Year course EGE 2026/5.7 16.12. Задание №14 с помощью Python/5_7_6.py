def f(n):
    return 6 ** 2030 + 6 ** 100 - n


res = []
for x in range(1, 2030):
    num = f(x)
    cnt = 0
    while num:
        num, r = divmod(num, 6)
        if r == 0:
            cnt += 1
    res.append(cnt)
print(max(res))