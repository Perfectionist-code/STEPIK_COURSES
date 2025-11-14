def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


for n in range(154026, 154043):
    divs = get_divisors(n)
    if len(divs) == 4:
        print(*sorted(divs)[-2:])
