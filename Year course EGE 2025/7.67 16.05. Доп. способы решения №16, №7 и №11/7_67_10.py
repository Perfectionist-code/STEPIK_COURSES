from math import ceil, log2

n = 25
k = 10 + 2 * 26 + 465
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 1500
V = 77 * 2 ** 10
for v_add in range(1, 1000):
    if (v + v_add) * N > V:
        print(v_add - 1)
        break
