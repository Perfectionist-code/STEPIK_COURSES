from math import ceil, log2

n = 8
k = 7
i = ceil(log2(k))
v_pas = ceil(n * i / 8)
v_add = 8
v = v_pas + v_add
N = 42
V = v * N
print('Ответ:', V, 'байт')
