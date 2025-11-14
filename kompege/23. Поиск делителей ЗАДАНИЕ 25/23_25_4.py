def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


cnt = 0
for n in range(150001, 10 ** 9):
    divs = get_divisors(n)
    if (s := sum(divs)) % 13 == 10:
        print(n, s)
        cnt += 1
    if cnt == 7:
        break
