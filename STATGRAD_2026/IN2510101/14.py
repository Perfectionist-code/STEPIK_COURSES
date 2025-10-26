from string import printable

d = {i: x for i, x in enumerate(printable[:29])}


def to_cs(num: int, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(d[r])
    return ''.join(res[::-1])


max_0 = 0
for x in range(1, 8411):
    n = 29 ** 293 + 29 ** 271 - x
    n_29 = to_cs(n, 29)
    if (l := n_29.count('0')) > max_0:
        max_0 = l
print(max_0)

# ОТВЕТ: 24 2 часа 3 мин