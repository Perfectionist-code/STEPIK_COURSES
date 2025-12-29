from itertools import permutations, product


def f(x, y, w, z) -> bool:
    return ((x or y) <= z) or (y == w) or z


for a1, a2, a3, a4 in product((0, 1), repeat=4):
    table = ((0, 1, a1, a2), (1, a3, 1, 0), (a4, 1, 1, 0))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
                print(*per, sep='')
