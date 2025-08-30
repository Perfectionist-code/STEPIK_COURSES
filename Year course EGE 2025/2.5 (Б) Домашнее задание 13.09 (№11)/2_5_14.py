from math import ceil

n = 300
N = 500_000
V = 40 * 2 << 19
for i in range(100):
    if ceil(n * i / 8) * N >= V:
        print('Ответ:', 2 ** (i - 1) + 1)
        break
