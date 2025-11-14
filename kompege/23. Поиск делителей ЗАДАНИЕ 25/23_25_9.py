def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


for n in range(1204300, 1204381):
    divs = [x for x in get_divisors(n) if not x % 2]
    if divs and (s := sum(divs)) % 10 == 0:
        print(n, s)
