from math import ceil, log2

k = 26 * 2 + 10
i = ceil(log2(k))
N = 1000
V = 10 * 2 ** 10
for n in range(1, 1000):
    if ceil(n * i / 8) * N > V:
        print('Ответ:', n - 1)
        break
