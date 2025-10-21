from math import prod


def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            return False
    return True


def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


ans = []
for n in range(125697, 190235):
    prime_divs = list(filter(lambda x: is_prime(x), get_divisors(n)))
    if prime_divs:
        if (pr := prod(prime_divs)) == n and len(prime_divs) == 2:
            ans.append(n)
print(len(ans), max(ans))
