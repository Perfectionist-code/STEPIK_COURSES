from math import ceil, log2

n = 12
k = 5
i = ceil(log2(k))
v = ceil(i * n / 8)
v_add = 11
N = 40
V = (v + v_add) * N
print(V)
