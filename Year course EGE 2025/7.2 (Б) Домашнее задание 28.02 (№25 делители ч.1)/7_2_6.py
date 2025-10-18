def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


cnt = 0
for n in range(800_000, 1_000_000):
    divs = list(filter(lambda x: x > 9 and x % 10 == 9, get_divisors(n)))
    if divs:
        print(n, divs[0])
        cnt += 1
    if cnt == 5:
        break
