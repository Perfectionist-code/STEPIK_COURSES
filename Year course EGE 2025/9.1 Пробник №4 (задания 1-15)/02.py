from itertools import product, permutations


def f(x, y, w, z):
    return (x <= y) and (z == (w <= x)) and (not w)


for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    table = ((0, a1, a2, 0), (1, 0, a3, a4), (a5, 1, a6, a7))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1, 1, 1]:
                print(*per, sep='')
