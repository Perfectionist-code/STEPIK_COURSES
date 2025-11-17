for n in range(2, 100):
    num = n ** 25 - 2 * n ** 13 + 10
    s = 0
    while num:
        num, r = divmod(num, n)
        s += r
    if s == 75:
        print(n)
        break
