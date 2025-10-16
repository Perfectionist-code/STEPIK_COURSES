def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


for n in range(164700, 164753):
    divs = get_divisors(n)
    if len(divs) == 6:
        print(*divs[-2:])
