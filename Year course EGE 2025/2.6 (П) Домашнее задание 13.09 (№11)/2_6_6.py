from math import ceil, log2

n1 = 11
k1 = 26
i1 = ceil(log2(k1))
i2 = bin(700)[2:].__len__()
v_id = ceil((n1 * i1 + i2) / 8)
N = 44
V = 880
for v_add in range(1000):
    if (v_id + v_add) * N == V:
        print('Ответ:', v_add, 'байт')
