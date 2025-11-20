from math import ceil, log2

n = 20
N = 600_000
V = 11 * 2 ** 20
for i in range(1, 10000):
    if ceil(i * n / 8) * N > V:
        print(2 ** (i - 1) + 1)
        break
