from math import ceil, log2

k = 10 + 27
i = ceil(log2(k))
N = 3548
V = 12 * 2 ** 10
for n in range(1, 1000):
    if ceil(i * n / 8) * N > V:
        print(n)
        break
