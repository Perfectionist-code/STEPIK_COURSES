def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


def is_prime(num: int) -> bool:
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            return False
    return True


for n in range(25317, 51238):
    prime_divs = [x for x in get_divisors(n) if is_prime(x)]
    if prime_divs and len(prime_divs) >= 6:
        print(n, max(prime_divs))
