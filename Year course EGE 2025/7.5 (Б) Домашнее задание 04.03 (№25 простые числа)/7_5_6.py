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
for n in range(450001, 500000):
    prime_divisors = [x for x in get_divisors(n) if is_prime(x)]
    if prime_divisors:
        m = max(prime_divisors) - min(prime_divisors)
    else:
        m = 0
    if m % 29 == 11:
        cnt +=1
        print(n, m)
    if cnt == 4:
        break
