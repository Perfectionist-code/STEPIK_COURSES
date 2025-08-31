from math import log2, ceil

k = 10 + 52 + 458
i = ceil(log2(k))

N = 862
V = 276 * 2 << 9
for n in range(1000):
    if ceil(n * i / 8) * N > V:
        print('Ответ:', n - 1)
        break
