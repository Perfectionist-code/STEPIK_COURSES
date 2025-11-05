from fnmatch import fnmatch


def get_divisors(num: int):
    divisors = {1, num}
    for d in range(2, int(num ** .5) + 1):
        if num % d == 0:
            divisors.add(d)
            divisors.add(num // d)
    return divisors


mask = '6*97*5?'
cnt = 0
for i in range(65000, 10 ** 10 + 1):
    n = str(i)
    if fnmatch(n, mask) and len(even_divs := [x for x in get_divisors(i) if x % 2 == 0]) >= 4:
        print(i, sum(even_divs))
        cnt += 1
    if cnt == 7:
        break
