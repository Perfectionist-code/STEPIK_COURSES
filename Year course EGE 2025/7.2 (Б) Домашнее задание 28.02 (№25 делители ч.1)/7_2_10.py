def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


cnt = 0
for n in range(900_000, 1000000):
    if divs := get_divisors(n):
        m = divs[-1] + divs[0]
        if m % 1000 == 112:
            print(n, m)
            cnt += 1
    if cnt == 5:
        break
