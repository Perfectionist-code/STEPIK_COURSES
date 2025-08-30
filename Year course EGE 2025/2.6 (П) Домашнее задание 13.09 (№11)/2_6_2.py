from math import ceil, log2

n = 303
k = 10 + 8190
i = ceil(log2(k))
v_id = ceil(n * i / 8)
N = 101
V = 101 * 2 ** 10
for v_add in range(1000):
    if (v_id + v_add) * N > V:
        print('Ответ:', v_add - 1, 'байт')
        break
