from math import ceil, log2

k = 30 + 1000
i = ceil(log2(k))
N = 4_915_540
V = 3 * 2 ** 30
for n in range(1, 10000):
    if ceil(n * i / 8) * N > V:
        print(n - 1)
        break
