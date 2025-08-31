from math import ceil, log2

n1 = 12
k1 = 26
i1 = ceil(log2(k1))
n2 = 5
k2 = 10
i2 = ceil(log2(k2))
v_id = ceil((n1 * i1 + n2 * i2) / 8)
N = 30
V = 2100
for v_add in range(1000):
    if (v_id + v_add) * N == V:
        print('Ответ:', v_add, 'байт')
        break
