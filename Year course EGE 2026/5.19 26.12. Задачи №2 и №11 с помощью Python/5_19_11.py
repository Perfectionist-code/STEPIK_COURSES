from math import ceil, log2

k = 16 + 4090
i = ceil(log2(k))
N = 3_221_540
V = 40 * 2 ** 30
for n in range(1, 10 ** 8):
    if ceil(i * n / 8) * N > V:
        print(n)
        break
