def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


cnt = 0
for n in range(700_001, 10 ** 10):
    divs = get_divisors(n)
    if 7 in divs:
        divs.remove(7)
    divs_end_7 = [x for x in divs if x % 10 == 7]
    if divs_end_7:
        cnt += 1
        print(n, min(divs_end_7))
    if cnt == 5:
        break
