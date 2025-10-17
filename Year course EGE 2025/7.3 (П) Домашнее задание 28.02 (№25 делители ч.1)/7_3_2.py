from math import prod


def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors) if len(divisors) >= 5 else False


cnt = 0
for n in range(200_000_001, 300_000_000):
    divs = get_divisors(n)
    # if divs:
    #     print(n, *divs)
    if divs and (p := prod(divs[:5])) % 10 == 1 and p <= n:
        cnt += 1
        print(p, divs[4])
    if cnt == 5:
        break
