from math import ceil, log2

n = 34
v_add = 28
N = 2000
V = 124 * 2 ** 10
for i in range(1, 1000):
    if (ceil(i * n / 8) + v_add) * N > V:
        print(2 ** (i - 1))
        break
