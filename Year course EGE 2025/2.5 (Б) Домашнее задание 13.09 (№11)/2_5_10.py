from math import ceil, log2

k = 10 + 2030
i = ceil(log2(k))
N = 318
V = 67 * 2 << 9
for n in range(1, 1000):
    if ceil(n * i / 8) * N >= V:
        print('Ответ:', n)
        break
