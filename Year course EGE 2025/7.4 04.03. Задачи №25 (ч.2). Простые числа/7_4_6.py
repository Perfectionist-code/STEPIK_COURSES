from math import prod

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
for n in range(1000000, 1, -1):
    if divs := get_divisors(n):
        prime_divs = list(filter(lambda x: is_prime(x), divs))
        if is_prime(pr:= prod(prime_divs)):
            print(n, pr)
            cnt += 1
    if cnt == 5:
        break
