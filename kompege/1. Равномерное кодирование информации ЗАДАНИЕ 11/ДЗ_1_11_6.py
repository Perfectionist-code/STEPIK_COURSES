from math import log2, ceil

n1 = 11
k1 = 15 + 10
i1 = ceil(log2(k1))
v1 = ceil(n1 * i1 / 8)
n2_1 = 5
k2_1 = 26
i2_1 = ceil(log2(k2_1))
v2_1 = n2_1 * i2_1
v2_2 = len(bin(999)[2:])
v2 = ceil((v2_1 + v2_2) / 8)
print('Ответ:', 30 - v1 - v2, 'байт')
