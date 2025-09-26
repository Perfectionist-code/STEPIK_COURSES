def num_to_cs(num, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(str(r))
    return ''.join(res[::-1])


def sum_figures(num):
    return sum(map(int, num))

for x in range(1000):
    num = 36 ** 17 - 6** x + 71
    num = num_to_cs(num, 6)
    if sum_figures(num) == 61:
        print(x)
        break