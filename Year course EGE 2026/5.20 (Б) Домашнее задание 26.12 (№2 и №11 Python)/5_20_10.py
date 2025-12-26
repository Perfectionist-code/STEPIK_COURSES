from math import ceil, log2

k = 10 + 52 + 963
i = ceil(log2(k))
N = 2000
V = 693 * 2 ** 10
for n in range(1, 10000):
    if ceil(n * i / 8) * N > V:
        print(n - 1)
        break
