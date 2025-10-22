from itertools import permutations, product


def f(x, y, w, z):
    return not w and ((y or z) <= (not x and y))


for p in product((0, 1), repeat=8):
    table = ((p[0], p[1], p[2], 1), (p[3], p[4], 1, p[5]), (p[6], 1, 1, p[7]))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1, 1, 1]:
                print(*per, sep='')
