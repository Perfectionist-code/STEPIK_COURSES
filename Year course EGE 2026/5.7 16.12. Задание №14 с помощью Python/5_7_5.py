def f(n):
    return 3 ** 100 - n


for x in range(2031, 0, -1):
    cnt = 0
    num = f(x)
    while num:
        num, r = divmod(num, 3)
        if r == 0:
            cnt += 1
    if cnt == 5:
        print(x)
        break