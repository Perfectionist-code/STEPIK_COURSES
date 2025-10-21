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
for n in range(250157, 1_000_000):
    if divs := get_divisors(n):
        try:
            A_even = max([x for x in divs if not x % 2])
            A_odd = max([x for x in divs if x % 2])
        except ValueError:
            continue
        A = abs(A_even - A_odd)
        if is_prime(A) and A % 10 == 9:
            cnt += 1
            print(n, A)
    if cnt == 5:
        break
