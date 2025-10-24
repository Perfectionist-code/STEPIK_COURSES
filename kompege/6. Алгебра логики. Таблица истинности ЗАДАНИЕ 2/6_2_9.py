from itertools import permutations


def f(x, y, w, z):
    return (y <= (x or z)) and (z <= y)


table = ((1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 0, 1), (0, 1, 1, 0))

for per in permutations('xywz'):
    if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0, 0]:
        print(*per)
