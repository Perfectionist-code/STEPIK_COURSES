from math import ceil, log2

n = 5
k = 10 + 7084
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 22_528
V = v * N // 2 ** 10
print(V)
