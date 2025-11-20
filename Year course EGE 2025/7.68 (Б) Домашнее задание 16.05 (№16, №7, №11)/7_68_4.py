from math import ceil, log2

k = 10 + 26 + 476
i = ceil(log2(k))
N = 5000
V = 2 ** 20
for n in range(1, 10000):
    if ceil(i * n / 8) * N > V:
        print(n - 1)
        break
