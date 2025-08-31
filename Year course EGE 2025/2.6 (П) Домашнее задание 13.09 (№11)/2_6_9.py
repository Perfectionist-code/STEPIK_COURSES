from math import ceil, log2

k1 = 6
i1 = ceil(log2(k1))
v1 = i1
n2 = 11
k2 = 20
i2 = ceil(log2(k2))
v2 = n2 * i2
v3 = len(bin(1999)[2:])
v_obj = ceil((v1 + v2 + v3) / 8)
N = 36
V = 1188
for v_add in range(1000):
    if (v_obj + v_add) * N == 1188:
        print('Ответ:', v_add, 'байт')
        break
