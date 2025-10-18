from math import prod


def find_divisors(num: int):
    cnt = 0
    res = []
    for d in range(2, num // 2 + 1):
        if not (num % d):
            if cnt == 2:
                return False
            cnt += 1
            res.append(d)
    return tuple(res)


result = []
for i in range(174457, 174506):
    if divisors := find_divisors(i):
        result.append(divisors)
result.sort(key=prod)
for tup in result:
    print(*tup)
