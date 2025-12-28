from math import ceil

def get_divisors(num):
    divisors = set()
    for d in range(1, int(num ** .5) + 1):
        if not num % d:
            divisors |= {d, num // d}
    return divisors


for n in range(ceil((113_000_000 // 2) ** 0.5), ceil((114_000_000 // 2) ** 0.5)):
    x = 2 * n ** 2
    even_divisors = sorted(x for x in get_divisors(x) if x % 2 == 0)
    if len(even_divisors) == 3:
        print(x, even_divisors[1])


