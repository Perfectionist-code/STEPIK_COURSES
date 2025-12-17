def f(n):
    return 27 ** 298 + 27 ** 269 - n


res = []
for x in range(1, 7290):
    num = f(x)
    cnt = 0
    while num:
        num, r = divmod(num, 27)
        if r == 0:
            cnt += 1
        res.append(cnt)
print(max(res))
