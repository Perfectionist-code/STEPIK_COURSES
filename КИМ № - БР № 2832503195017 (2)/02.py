from itertools import permutations, product, repeat


def f(x, y, w, z):
    return ((y and (x == (not z))) <= w) and (z <= y)


for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    table = ((0, 0, a1, a2), (0, a3, 0, 0), (1, a4, a5, 1))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
                print(*per, sep='')
