from itertools import product, permutations


def f(x, y, w, z):
    return not not (x <= y) or ()


for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    table = ((0, 0, a1, a2), (a3, a4, 1, a5), (a6, 1, 0, a7))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
                print(*per, sep='')
