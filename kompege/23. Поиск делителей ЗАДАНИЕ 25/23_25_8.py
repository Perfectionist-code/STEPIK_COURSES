def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


for n in range(190201, 190261):
    divs = sorted([x for x in get_divisors(n) if not x % 2])
    if len(divs) == 4:
        print(*divs[-2:][::-1])
