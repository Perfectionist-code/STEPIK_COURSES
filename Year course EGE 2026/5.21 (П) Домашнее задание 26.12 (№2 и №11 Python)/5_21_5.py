from itertools import product, permutations


def f(x, y, w, z):
    return w and ((z or y) == (z and x))


for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    table = ((1, a1, 1, 0), (0, a2, a3, a4), (1, 1, 1, a5))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1, 1, 0]:
                print(*per, sep='')
