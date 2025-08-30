from math import ceil, log2

n = 9
k = 10 + 29 * 2
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 20
V = v * N
print('Ответ:', V, 'байт')
