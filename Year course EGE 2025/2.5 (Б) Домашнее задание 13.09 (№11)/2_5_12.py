from math import ceil

n = 500
N = 200_000
V = 80 * 2 ** 20
for i in range(100):
    if ceil(n * i / 8) * N >= V:
        print('Ответ:', 2 ** (i - 1))
        break
