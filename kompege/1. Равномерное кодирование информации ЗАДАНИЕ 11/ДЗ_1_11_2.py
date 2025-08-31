from math import log2, ceil

n = 7
k = 12
i = ceil(log2(k))
v = ceil(n * i / 8)
v_add = 15
N = 150
V = (v + v_add) * N
print('Ответ', V, 'байт')
