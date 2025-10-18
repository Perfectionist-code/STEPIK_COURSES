def get_divisors(num: int):
    res = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            res.add(d)
            res.add(num // d)
    return sorted(res)


cnt = 0
for n in range(500000, 1_000_000):
    for div in get_divisors(n):
        if div > 8 and div % 10 == 8:
            print(n, div)
            cnt += 1
            break
    if cnt == 5:
        break
