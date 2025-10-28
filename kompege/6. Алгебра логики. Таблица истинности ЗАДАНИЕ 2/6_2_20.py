from itertools import product, permutations


def f(x, y, w, z):
    return (x == (not z)) <= ((x or w) == y)


for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    table = ((0, a1, 0, a2), (a3, a4, 0, 0), (a5, 0, 0, 0))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [0,0,0]:
                print(*per, sep="")
