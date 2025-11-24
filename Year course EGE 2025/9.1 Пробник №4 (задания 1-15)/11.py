from math import ceil, log2

k = 10 + 1015
i = ceil(log2(k))
N = 3000
V = 555 * 2 ** 10
for n in range(1, 1000):
    if ceil(n * i / 8) * N > V:
        print(n - 1)
        break
