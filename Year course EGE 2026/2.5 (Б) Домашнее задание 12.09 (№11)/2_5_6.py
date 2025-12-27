from math import ceil, log2

n = 14
k = 26 * 2
i = ceil(log2(k))
v = ceil(i * n / 8)
V = 600
N = V // v
print(N)
