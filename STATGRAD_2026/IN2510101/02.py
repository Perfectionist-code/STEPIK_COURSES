from itertools import permutations, product


def f(x, y, w, z):
    return ((not x) and z and (not y) and (not w)) or ((not x) and z and y and (not w)) or ((not x) and z and y and w)


for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    table = ((a1, 1, 0, a2), (0, 0, a3, a4), (a5, a6, 1, a7))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1, 1, 1]:
                print(*per, sep='')

# xywz
