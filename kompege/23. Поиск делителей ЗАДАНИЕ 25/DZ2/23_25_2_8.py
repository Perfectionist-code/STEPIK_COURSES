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
mask = '?6*6*?6'
for n in range(1000, 10 ** 9):
    if fnmatch(str(n), mask) and n % 6 == 0 and n % 7 == 0 and n % 8 == 0:
        cnt += 1
        res.append((n, sum(get_divisors(n))))
    if cnt == 7:
        break
res.sort()
for p in res:
    print(*p)
