from math import ceil, log2

n = 7
k = 26 * 2
i = ceil(log2(k))
v = ceil(i * n / 8)
v_add = 12
V = 2 * 2 ** 10
for N in range(1, 1000):
    if (v + v_add) * N > V:
        print(N - 1)
        break
