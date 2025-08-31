from math import ceil, log2

n1 = 15
k1 = 26
i1 = ceil(log2(k1))
v_id = ceil(n1 * i1 / 8)
n2 = 20
i2 = len(bin(2023)[2:])
v_description = ceil(n2 * i2 / 8)
v_obj = v_id + v_description
N = 65_536
V = 4 * 2 ** 20
for v_add in range(100000):
    if (v_obj + v_add) * N == V:
        print('Ответ:', v_add, 'байт')
        break
