def get_divisors(num: int):
    res = set()
    for d in range(2, num // 2 + 1, 2):
        if not num % d:
            res.add(d)
    s = sum(res)
    if s and not s % 10:
        return num, s
    else:
        return False

for n in range(1204300, 1204381):
    if dv:=get_divisors(n):
        print(*dv)
