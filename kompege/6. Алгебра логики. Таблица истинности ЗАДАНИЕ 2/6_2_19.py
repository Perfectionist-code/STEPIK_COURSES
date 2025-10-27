from itertools import permutations, product


def f(x, y, z, w):
    return (x and z) or ((w <= x) == (z <= y))


for a1, a2, a3, a4, a5, a6 in product((0, 1), repeat=6):
    table = ((a1, a2, a3, 1), (a4, a5, 1, 1), (a6, 1, 1, 1))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
                print(*per, sep="")
