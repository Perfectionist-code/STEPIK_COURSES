def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
        if len(divisors) > 3: return False
    return divisors


for n in range(106732567, 152673837):
    divs = get_divisors(n)
    if divs and len(divs) == 3:
        print(n, max(divs))
