from itertools import permutations, product


def f(x, y, w, z):
    return ((z <= x) and (x <= w)) or (y == (z or x))


for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    table = ((a1, 1, a2, a3), (a4, a5, 1, 1), (a6, 1, a7, 1))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
                print(*per, sep='')
