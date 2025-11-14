from fnmatch import fnmatch


def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** .5) + 1):
        if num % d == 0:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


res = []
cnt = 0
mask = '9?*55*7'
for n in range(10 ** 7, 0, -1):
    if fnmatch(str(n), mask):
        cnt += 1
        divs_sum = sum(get_divisors(n))
        res.append((n, divs_sum % 21))
    if cnt == 5:
        break
res.sort()
for p in res:
    print(*p)
