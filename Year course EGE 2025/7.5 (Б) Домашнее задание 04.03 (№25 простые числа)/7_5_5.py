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


cnt = 0
for n in range(250001, 500000):
    s = sum((x for x in get_divisors(n) if is_prime(x)))
    if s and not s % 17:
        print(n, s)
        cnt += 1
    if cnt == 5:
        break
