from math import ceil, log2

n = 15
k = 12
i = ceil(log2(k))
v = ceil(i * n / 8)
V = 400
N = 20
for v_add in range(1, 1000):
    if (v + v_add) * N == V:
        print(v_add)
        break
