from itertools import permutations, product


def f(x, y, w, z):
    return ((w <= y) or not (y <= z)) and not x and not (x == z)


for p in product((0, 1), repeat=5):
    table = ((0, p[0], 1, p[1]), (1, p[2], p[3], 1), (0, p[4], 1, 1))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1,1,1]:
                print(*per, sep='')
