def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


cnt = 0
for n in range(300001, 10 ** 9):
    divs = [x for x in get_divisors(n) if x % 3 == 0]
    if len(divs) == 5:
        print(n, max(divs))
        cnt += 1
    if cnt == 4:
        break
