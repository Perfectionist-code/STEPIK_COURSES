g = 9 ** 1942 + 9 * 6 ** 971 + 214

for x in range(1, 10 ** 10):
    num = g - x
    cnt = 0
    while num:
        num, r = divmod(num, 9)
        if r == 2:
            cnt += 1
        if r == 8:
            cnt -= 1
    if abs(cnt) == 471:
        print(x)
        break
