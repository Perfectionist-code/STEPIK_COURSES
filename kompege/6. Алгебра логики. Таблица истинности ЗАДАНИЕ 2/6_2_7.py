from itertools import permutations


def f(x, y, z):
    return (not x and y and z) or (not x and not z)


table = ((0, 0, 0), (1, 0, 0), (1, 1, 0))

for per in permutations('xyz'):
    if [f(**dict(zip(per, row))) for row in table] == [1, 1, 1]:
        print(*per)
