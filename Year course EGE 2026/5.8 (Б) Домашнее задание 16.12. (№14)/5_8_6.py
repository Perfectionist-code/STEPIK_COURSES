def f(n):
    return 7 ** 100 - n


for x in range(5000, 10 ** 10):
    num = f(x)
    cnt = 0
    while num:
        num, r = divmod(num, 7)
        if r == 0:
            cnt += 1
    if cnt == 5:
        print(x)
        break
