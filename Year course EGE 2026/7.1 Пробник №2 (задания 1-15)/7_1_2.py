from itertools import product, permutations


def f(x, y, w, z):
    return x <= (not ((y <= z) and (z == (not w))))


for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    table = ((0, a1, a2, 0), (a3, 1, 1, a4), (a5, 1, 0, 0))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
                print(*per, sep='')
