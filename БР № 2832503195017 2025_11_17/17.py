def is_consist_chet(num: int) -> bool:
    num = str(num)
    return all(x in '02468' for x in num)


def is_consist_nechet(num: int) -> bool:
    num = str(num)
    return all(x in '13579' for x in num)


with open('17_5916.txt') as file:
    sums = []
    a = [int(x) for x in file]
    for x, y in zip(a, a[1:]):
        cn_cnt = is_consist_chet(x) + is_consist_chet(y)
        nch_cnt = is_consist_nechet(x) + is_consist_nechet(y)
        if cn_cnt == 1 and nch_cnt == 1:
            sums.append((x + y, x, y))
            print(f'{x} + {y} = {x + y}')
print('----' * 10)
print(len(sums), max(sums)[0])
