from math import ceil, log2

n = 2783
N = 62_784
V = 356 * 2 ** 20
for i in range(1, 1000):
    if ceil(i * n / 8) * N > V:
        print(2 ** (i - 1) + 1)
        break
