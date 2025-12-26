from itertools import product, permutations


def f(x, y, w, z):
    return not (y and (not x)) and not (x == z) and w


for a1, a2, a3, a4 in product((0, 1), repeat=4):
    table = ((0, 0, a1, 1), (0, 1, 0, 1), (a2, a3, 0, a4))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1, 1, 1]:
                print(*per, sep='')
