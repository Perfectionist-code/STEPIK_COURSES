from statistics import mean


def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


cnt = 0
for n in range(550001, 10 ** 9):
    divs = get_divisors(n)
    if divs and (f := int(mean(divs))) % 31 == 13:
        print(n, f)
        cnt += 1
    if cnt == 5:
        break
