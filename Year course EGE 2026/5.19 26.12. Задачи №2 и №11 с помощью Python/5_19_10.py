from math import ceil, log2

k = 16 + 52 + 1980
i = ceil(log2(k))
N = 5_321_440
V = 100 * 2 ** 30
for n in range(1, 10 ** 8):
    if ceil(i * n / 8) * N > V:
        print(n - 1)
        break
