from math import log2, ceil

n = 15
k = 8
i = ceil(log2(k))
v = ceil(n * i / 8)
v_add = 24
N = 20
V = (v + v_add) * N
print('Ответ:', V, 'байт')
