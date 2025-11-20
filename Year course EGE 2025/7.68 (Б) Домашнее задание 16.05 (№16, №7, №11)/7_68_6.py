from math import ceil, log2

n = 10
k = 26
i = ceil(log2(k))
V = 4 * 2 ** 10
for N in range(1, 10000):
    if (ceil(i * n / 8) + 15) * N > V:
        print(N - 1)
        break
