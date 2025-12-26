from math import ceil, log2

n = 2430
k = 10 + 26 * 2
N = 1_350_400
V = 5 * 2 ** 30
for k1 in range(1, 10000):
    i = ceil(log2(k + k1))
    if ceil(n * i / 8) * N > V:
        print(k1 - 1)
        break
