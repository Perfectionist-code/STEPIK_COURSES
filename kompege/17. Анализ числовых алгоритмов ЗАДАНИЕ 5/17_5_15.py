from math import prod


def get_r(n: int):
    n_l = [int(x) for x in str(n)]
    r = sorted((prod(n_l[:2]), prod(n_l[1:])), reverse=True)
    r = str(r[0]) + str(r[1])
    return int(r)


for num in range(999, 99, -1):
    if get_r(num) == 240:
        print(num)
        break
