from math import ceil, log2

n = 261
N = 252_500
V = 31 * 2 ** 20
for i in range(1, 100):
    if ceil(n * i / 8) * N >= V:
        print('Ответ:', 2 ** (i - 1) + 1)
        break
