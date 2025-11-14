def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


cnt = 0
for n in range(550_001, 10 ** 9):
    divs = [x for x in get_divisors(n) if x % 10 == 7]
    if len(divs) == 3:
        print(n, max(divs))
        cnt += 1
    if cnt == 5:
        break
