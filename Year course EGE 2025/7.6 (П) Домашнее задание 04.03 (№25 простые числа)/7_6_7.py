from math import prod


def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            return False
    return True


def get_divisors(num: int) -> set:
    divisors = set()
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


ans = []
for n in range(173225, 217438):
    prime_divisors = list(filter(lambda x: is_prime(x), get_divisors(n)))
    if prime_divisors and len(prime_divisors) == 2 and prod(prime_divisors) == n and str(prime_divisors[0])[-1] == \
            str(prime_divisors[1])[-1]:
        ans.append((n, prime_divisors))
print(len(ans), min(ans)[0])
