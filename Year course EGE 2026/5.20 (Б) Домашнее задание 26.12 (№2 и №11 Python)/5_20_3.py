from itertools import product, permutations


def f(x, y, w, z):
    return (x <= y) and z and (not w)


for a1, a2, a3, a4, a5, a6 in product((0, 1), repeat=6):
    table = ((0, 1, a1, a2), (1, 1, a3, a4), (1, a5, 1, a6))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1, 1, 1]:
                print(*per, sep='')
