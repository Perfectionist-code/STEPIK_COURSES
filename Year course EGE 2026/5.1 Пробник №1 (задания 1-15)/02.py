from itertools import product, permutations


def f(a, b, c, d):
    return c and (a or d) and (d <= b)


for a1, a2, a3, a4, a5, a6 in product((0, 1), repeat=6):
    table = ((a1, a2, a3, 0), (a4, 1, 0, a5), (0, a6, 1, 0))
    if len(table) == len(set(table)):
        for per in permutations('abcd'):
            if [f(**dict(zip(per, row))) for row in table] == [1, 1, 1]:
                print(*per, sep='')
