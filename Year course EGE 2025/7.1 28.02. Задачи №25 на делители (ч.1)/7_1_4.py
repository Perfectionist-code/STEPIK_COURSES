def get_divisors(num: int):
    res = []
    for d in range(2, num // 2 + 1):
        if not num % d:
            res.append(d)
    s = sum(res)
    if not res:
        return False
    return (False, (num, s // 13))[not s % 13]


cnt = 0
for n in range(350300, 100_000_000):
    if dv := get_divisors(n):
        if cnt < 6:
            cnt += 1
            print(*dv)
        else:
            break
