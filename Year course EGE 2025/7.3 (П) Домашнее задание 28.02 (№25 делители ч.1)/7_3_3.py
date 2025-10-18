from math import sqrt


def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


cnt = 0
for n in range(107108, 1_000_000):
    divs = get_divisors(n)
    res = list(filter(lambda x: sqrt(x).is_integer(), divs))
    if len(res) == 3:
        print(n, max(res), res)
        cnt += 1
    if cnt == 5:
        break
