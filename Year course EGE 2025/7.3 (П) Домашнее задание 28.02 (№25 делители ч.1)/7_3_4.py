from math import sqrt


def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


cnt = 0
for n in range(10_000_001, 20_000_000):
    if len(divs := get_divisors(n)) >= 3:
        s = sum(divs[-3:])
        if sqrt(s).is_integer():
            cnt += 1
            print(n, s)
    if cnt == 5:
        break
