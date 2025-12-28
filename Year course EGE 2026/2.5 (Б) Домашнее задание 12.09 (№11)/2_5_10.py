from math import ceil, log2

n = 105
k = 10 + 1500
i = ceil(log2(k))
v = ceil(i * n / 8)
N = 16_384
V = v * N // 2 ** 10
print(V)
