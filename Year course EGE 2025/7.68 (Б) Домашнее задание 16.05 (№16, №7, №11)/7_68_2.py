from math import ceil, log2

n = 119
N = 125_300
V = 23 * 2 ** 20
for i in range(1, 1000):
    if ceil(i * n / 8) * N > V:
        print(2 ** (i - 1) + 1)
        break
