def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


for n in range(397438, 443521):
    divs = get_divisors(n)
    even_divisor = sorted(filter(lambda x: not x % 2, divs))
    if (lv:=even_divisor.__len__()) >= 142:
        print(lv, max(even_divisor))
