from math import ceil, log2

n = 400
N = 100_000
V = 50 * 2 ** 20
for i in range(1, 100):
    if ceil(n * i / 8) * N >= V:
        print('Ответ:', 2 ** (i - 1))
        break
