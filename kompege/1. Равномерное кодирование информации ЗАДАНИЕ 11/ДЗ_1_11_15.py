from math import log2, ceil

n = 745
k = 10 + 999
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 312
V = 311 * 2 << 9
for v_add in range(1, 1000):
    if (v + v_add) * N > V:
        print('Ответ:', (v_add - 1) * N, 'байт')
        break

