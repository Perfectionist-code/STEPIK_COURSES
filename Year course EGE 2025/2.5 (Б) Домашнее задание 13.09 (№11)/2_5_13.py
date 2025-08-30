from math import ceil

n = 600
N = 150_000
V = 60 * 2 ** 20
for i in range(100):
    if ceil(n * i / 8) * N >= V:
        print('Ответ:', 2 ** (i - 1))
        break
