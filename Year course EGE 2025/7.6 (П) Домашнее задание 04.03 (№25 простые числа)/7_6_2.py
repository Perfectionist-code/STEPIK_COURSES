def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            return False
    return True


def get_divisors(num: int) -> list:
    divisors = set()
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


cnt = 0
res = []
for n in range(55000001, 75000001):
    if divs := get_divisors(n):
        prime_divs = [x for x in divs if is_prime(x) and x % 1000 == 777]
        if prime_divs:
            cnt += 1
            res.append((n, min(prime_divs)))
    if cnt == 4:
        break
res = sorted(res, key=lambda x: x[1])
for tp in res:
    print(*tp)
