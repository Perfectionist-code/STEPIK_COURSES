from math import ceil, log2

n = 24
N = 5100
V = 170 * 2 ** 10
for k_s in range(1, 10 ** 12):
    k = 10 + 2 * 26 + k_s
    i = ceil(log2(k))
    if ceil(n * i / 8) * N > V:
        print(k_s - 1)
        break
