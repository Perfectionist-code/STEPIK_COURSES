from math import ceil, log2

n = 23
k = 10 + 2 * 26
i = ceil(log2(k))
v = ceil(n * i / 8) + 10
V = 20 * 2 ** 10
for N in range(1, 1000):
    if v * N > V:
        print(N - 1)
        break
