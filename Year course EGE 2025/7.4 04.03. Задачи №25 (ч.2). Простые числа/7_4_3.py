def is_prime(num: int) -> bool:
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


max_prime_divisors = 0
max_prime_divs = []
for n in range(2,10_000_001):
    prime_divs = list(filter(lambda x: is_prime(x), get_divisors(n)))
    if (lpd:=len(prime_divs)) > max_prime_divisors:
        max_prime_divs = [(n, lpd)]
        max_prime_divisors = lpd
    elif lpd == max_prime_divisors:
        max_prime_divs.append((n, lpd))
    if n % 100_000 == 0:
        print(n, max_prime_divisors)
print(*min(max_prime_divs))
print(*max_prime_divs)