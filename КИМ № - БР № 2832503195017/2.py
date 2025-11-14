from itertools import permutations, product


def f(x,y,w,z):
    return (x <= y) and (y <= z) and (z <= w)


for a1, a2, a3, a4, a5, a6 in product((0, 1), repeat=6):
    table = ((a1, 0, 1, a2), (a3, 1, a4, 0), (a5, 0, 1, a6))
    if len(table) == len(set(table)):
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1,1,1]:
                print(*per, sep='')
