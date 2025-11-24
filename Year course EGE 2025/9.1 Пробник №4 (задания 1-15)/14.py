for x in range(5769, 1, -1):
    num = 9 ** 2025 + 9 ** 1000 - x
    cnt = 0
    while num:
        num, r = divmod(num, 9)
        if r == 0:
            cnt += 1
    if cnt == 1026:
        print(x)
        break
