from math import ceil, log2

n = 60
k = 10 + 250
i = ceil(log2(k))
N = 65_536
v = ceil(i * n / 8) * N
print(v // 2 ** 10)
