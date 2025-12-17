def f(n):
    return 7 ** 170 + 7 ** 100 - n


for x in range(2030, 0, -1):
    cnt = 0
    num = f(x)
    while num:
        num, r = divmod(num, 7)
        if r == 0:
            cnt += 1
    if cnt == 71:
        print(x)
        break