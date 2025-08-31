from math import log2, ceil

n = 20
k = 2 + 8
i = ceil(log2(k))
v = ceil(i * n / 8)
v_ip = 4
N = 192
V = 6 * 2 << 9
for v_add in range(1000):
    if (v + v_ip + v_add) * N == V:
        print('Ответ:', v_add, 'байт')
        break
