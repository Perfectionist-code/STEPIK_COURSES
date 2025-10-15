def get_divisors(num: int):
    res = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            res.add(d)
            res.add(num // d)
    return sorted(res)


cnt = 0
for n in range(424_242, 700_000):
    divisors = get_divisors(n)
    if divisors.__len__() > 1:
        m = max(divisors) + min(divisors)
    else:
        m = 0
    if m % 2024 == 42:
        cnt += 1
        print(n, m)
    if cnt == 8:
        break
