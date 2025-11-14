def is_prime(num: int):
    if num == 1: return False
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            return False
    return True


def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


cnt = 0
for n in range(5_400_001, 10 ** 9):
    divs = get_divisors(n)
    prime_divs = [x for x in divs if is_prime(x)]
    if prime_divs and (m := max(prime_divs) + min(prime_divs)) > 60000:
        str_m = str(m)
        if str_m == str_m[::-1]:
            cnt += 1
            print(n, m)
    if cnt == 5:
        break
