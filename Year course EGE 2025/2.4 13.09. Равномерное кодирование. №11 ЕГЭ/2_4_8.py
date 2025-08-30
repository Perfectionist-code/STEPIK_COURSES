from math import ceil, log2

k = 26 + 10 + 8164
i = ceil(log2(k))
N = 835
V = 156 * 2 ** 10
for n in range(1, 1000):
    if ceil(n * i / 8) * N >= V:
        print('Ответ:', n)
        break
