def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors

for n in range(81234, 134690):
    divs = get_divisors(n)
    if len(divs) == 3:
        print(*sorted(divs))