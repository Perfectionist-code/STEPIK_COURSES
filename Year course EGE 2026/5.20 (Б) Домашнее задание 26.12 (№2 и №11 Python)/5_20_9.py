from math import ceil, log2

n = 3321
N = 2_563_328
v_add = 25
V = 15 * 2 ** 30
for i in range(1, 1000):
    if (ceil(n * i / 8) + v_add) * N > V:
        print(2 ** (i - 1) + 1)
        break
