from math import ceil, log2

n = 331
k = 10 + 900
i = ceil(log2(k))
v = ceil(i * n / 8)
N = 1536
print(v * N // 2 ** 10)
