from math import ceil, log2

n = 223
k = 10 + 26 + 32724
i = ceil(log2(k))
v = ceil(n * i / 8)
V = 17 * 2 ** 30
for N in range(1, 10 ** 12):
    if v * N > V:
        print(N - 1)
        break
