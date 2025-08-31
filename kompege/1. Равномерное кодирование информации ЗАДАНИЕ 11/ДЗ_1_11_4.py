from math import log2, ceil

n = 11
k = 2 * 26 + 10
i = ceil(log2(k))
v = ceil(n * i / 8)
v_add = 13
V = 2 << 9
for N in range(1000):
    if (v + v_add) * N > V:
        print('Ответ:', N - 1)
        break
