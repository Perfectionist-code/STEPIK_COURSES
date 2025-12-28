from math import ceil, log2

n = 8
k = 7
i = ceil(log2(k))
v_add = 8
N = 42
v = (ceil(i * n / 8) + v_add) * N
print(v)
