from math import ceil, log2

n = 9
k = 10 + 29 * 2
i = ceil(log2(k))
N = 20
v = ceil(i * n / 8) * N
print(v)
