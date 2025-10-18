from math import prod


def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


res_divs = []
for n in range(174457, 174506):
    divs = get_divisors(n)
    if len(divs[1:-1]) == 2:
        res_divs.append(divs[1:-1])
res_divs.sort(key=prod)
for d in res_divs:
    print(*d)
