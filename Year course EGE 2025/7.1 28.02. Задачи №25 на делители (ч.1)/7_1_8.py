def get_divisors(num: int):
    res = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            res.add(d)
            res.add(num // d)
    return sorted(res)


cnt = 0
for n in range(550000, 700_000):
    divisors = get_divisors(n)
    if divisors:
        divisors_7 = sorted(filter(lambda x: x % 10 == 7, divisors))
        if divisors_7.__len__() == 3:
            print(n, divisors_7[-1])
            cnt += 1
    if cnt == 5:
        break
