from math import ceil, log2

n = 3000
k = 10_000
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 2 ** 20
V = v * N // 2 ** 10
print(V)
