from itertools import permutations, product


def f(x, y, w, z):
    return (y <= x) or not ((x <= z) and (z <= x)) and not w


for pr in product((0, 1), repeat=6):
    table = ((0, 0, 0, pr[0]), (pr[1], 0, 0, pr[2]), (pr[3], pr[4], 0, pr[5]))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
                print(*per, sep='')
