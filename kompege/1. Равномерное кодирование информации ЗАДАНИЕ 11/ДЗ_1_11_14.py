from math import log2, ceil

n = 99
k = 10 + 510
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 4322
V = 543 * 2 << 9
for v_add in range(1000):
    if (v + v_add) * N > V:
        print('Ответ:', v_add, 'байт')
        break