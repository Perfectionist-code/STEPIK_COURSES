from math import ceil, log2

n = 257
N = 295_740
V = 33 * 2 ** 20
for i in range(1, 1000):
    if ceil(i * n / 8) * N > V:
        print(2 ** (i - 1))
        break
