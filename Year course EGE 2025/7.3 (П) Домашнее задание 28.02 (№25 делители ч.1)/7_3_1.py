def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return tuple(divisors)


cnt = 0
for k in range(1, 100_000):
    n = 750_000 + k
    divs = tuple(filter(lambda x: not x % 2, get_divisors(n)))
    if (ld := len(divs)) % 2:
        cnt += 1
        print(k, ld)
    if cnt == 5:
        break
