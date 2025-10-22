from itertools import permutations


def f(x, y, z):
    return not (x == (y <= z))


table = ((0, 0, 1), (0, 1, 1))
for per in permutations('xyz'):
    if [f(**dict(zip(per, row))) for row in table] == [1, 0]:
        print(*per)
