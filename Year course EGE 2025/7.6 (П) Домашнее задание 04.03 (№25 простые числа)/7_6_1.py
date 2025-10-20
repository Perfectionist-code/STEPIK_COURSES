from math import prod


def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            return False
    return True


def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


def cond_1(nums: set) -> bool:
    s = sum(nums)
    p = prod(nums)
    return s % 2 != 0 and p % 2 != 0


cnt = 0
for n in range(2000001, 4000000):
    if cond_1(divs := get_divisors(n)) and len(divs) > 30:
        cnt += 1
        prime_divs = [x for x in divs if is_prime(x)]
        print(n, max(prime_divs))
    if cnt == 6:
        break
