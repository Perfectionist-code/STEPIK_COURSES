from math import ceil, prod


def find_dividers(num: int) -> tuple:
    cnt = 0
    res = []
    for i in range(2, ceil(num / 2) + 1):
        if not num % i:
            cnt += 1
            if cnt > 2:
                return tuple()
            res.append(i)
    if cnt <= 1:
        return tuple()
    return tuple(res)


lst = []
for n in range(174457, 174505):
    if (r := find_dividers(n)):
        lst.append(r)
    lst.sort(key=prod)
for tup in lst:
    print(*tup, prod(tup))
