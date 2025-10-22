from itertools import permutations


def f(x, y, w, z):
    return not y and x and (not z or w)


table = ((0, 1, 0, 0), (1, 1, 0, 0), (1, 1, 1, 0))

for per in permutations('xywz'):
    if [f(**dict(zip(per, row))) for row in table] == [1, 1, 1]:
        print(*per)
