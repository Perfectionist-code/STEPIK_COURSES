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


cnt = 0
for n in range(500_000, 0, -1):
    prime_divs = [x for x in get_divisors(n) if is_prime(x)]
    if prime_divs and (s := sum(prime_divs)) % 10 == 0:
        print(n, s)
        cnt += 1
    if cnt == 7:
        break
