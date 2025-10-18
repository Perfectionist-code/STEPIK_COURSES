def get_divisors(num: int):
    res = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            res.add(d)
            res.add(num // d)
    if res:
        m = sum((max(res), min(res)))
    else:
        m = 0
    return (False, (num, m))[m % 10 == 4]


cnt = 0
for n in range(220_000, 1_000_000):
    if dv := get_divisors(n):
        cnt += 1
        print(*dv)
    if cnt == 5:
        break
