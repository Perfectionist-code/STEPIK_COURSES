def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


res_divs = []
for n in range(114578, 114617):
    divs = get_divisors(n)
    r = sum(filter(lambda x: x % 10 == 8, divs[1:-1]))
    if r % 10 == 6:
        print(n, r)
