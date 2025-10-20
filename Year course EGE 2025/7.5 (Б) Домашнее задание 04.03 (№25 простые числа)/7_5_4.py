def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for d in range(2, int(num ** .5) + 1):
        if num % d == 0:
            return False
    return True

def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


ans = []
max_len = 0
for n in range(2, 20001):
    prime_divs = list(filter(lambda x: is_prime(x), get_divisors(n)))
    if (ld := len(prime_divs)) > max_len:
        ans = [n]
        max_len = ld
    elif ld == max_len:
        ans.append(n)
print(ans)
print(min(ans), max_len)
