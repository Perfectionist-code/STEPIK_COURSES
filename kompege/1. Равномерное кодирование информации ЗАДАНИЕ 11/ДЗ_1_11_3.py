from math import log2, ceil

n = 9
k = 10 + 2 * 26 + 6
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 20
V = 500
for v_add in range(1000):
    if (v + v_add) * N == V:
        print('Ответ:', v_add, 'байт')
        break
