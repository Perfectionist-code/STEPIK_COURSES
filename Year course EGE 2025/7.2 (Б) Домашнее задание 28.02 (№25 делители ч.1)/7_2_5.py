def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


cnt = 0
for n in range(800_000, 1_000_000):
    divs = get_divisors(n)
    if len(divs) > 2:
        m = divs[1] + divs[-2]
    else:
        m = 0
    if m % 10 == 4:
        cnt += 1
        print(n, m)
        if cnt == 5:
            break
