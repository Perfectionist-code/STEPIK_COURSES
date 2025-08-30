from math import ceil, log2

k = 10 + 52 + 963
i = ceil(log2(k))
N = 2000
V = 693 * 2 << 9
for n in range(1, 500):
    if ceil(i * n / 8) * N > V:
        print('Ответ:', n - 1)
        break