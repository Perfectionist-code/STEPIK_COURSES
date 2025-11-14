from math import prod


def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


def is_prime(num: int) -> bool:
    if num == 1: return False
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            return False
    return True


for n in range(125697, 125722):
    divs = get_divisors(n)
    if len(divs) == 2 and all(is_prime(x) for x in divs) and prod(divs) == n:
        print(*sorted(divs))
