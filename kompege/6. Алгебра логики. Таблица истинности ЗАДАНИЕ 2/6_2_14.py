from itertools import permutations


def f(x, y, w, z):
    return (x <= y) or (not (w <= z))


table = ((1, 0, 0, 1), (0, 0, 0, 1), (1, 0, 1, 1))

for per in permutations('xywz'):
    if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
        print(*per, sep='')
