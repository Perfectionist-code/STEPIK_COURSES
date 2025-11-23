from itertools import product, permutations


def f(x, y, w, z):
    return not ((((((w and x) == x) or 1) <= z) or (not x)) and y)


for a1, a2, a3, a4 in product((0, 1), repeat=4):
    table = ((a1, a2, 1, 0), (1, a3, 1, 0), (a4, 0, 0, 1))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
                print(*per, sep='')
