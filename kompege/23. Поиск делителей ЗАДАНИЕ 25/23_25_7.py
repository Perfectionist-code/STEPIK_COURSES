from math import prod


def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


cnt = 0
for n in range(400_000_000, 10 ** 18):
    divs = sorted(get_divisors(n))[:5]
    if len(divs) >= 5 and (p := prod(divs)) % 100 == 17 and p <= n:
        print(p, divs[-1])
        cnt += 1
    if cnt == 5:
        break
