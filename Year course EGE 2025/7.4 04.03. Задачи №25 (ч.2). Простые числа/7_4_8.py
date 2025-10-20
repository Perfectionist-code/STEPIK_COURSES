def is_prime(num: int) -> bool:
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


cnt = 0
for n in range(23600000, 33600000):
    if divs := get_divisors(n):
        prime_divs = list(filter(lambda x: is_prime(x), divs))
        if (m:=max(prime_divs) + min(prime_divs)) % 213 == 171:
            print(n, m)
            cnt += 1
    if cnt == 6:
        break
