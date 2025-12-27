from math import ceil, log2

n = 107
k = 10 + 2090
i = ceil(log2(k))
N = 32_768
v = ceil(i * n / 8) * N
print(v // 2 ** 10)
