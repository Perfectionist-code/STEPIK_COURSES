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
mask = '14?4*'
for n in range(46082 * 217, 0, -217):
    if fnmatch(str(n), mask):
        cnt += 1
        divs = get_divisors(n)
        sum_odd_divs = sum((x for x in divs if x % 2))
        res.append((n, sum_odd_divs))
        if cnt == 7:
            break
res.sort()
for p in res:
    print(*p)
