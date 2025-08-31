from math import log2, ceil

n = 86
k = 250
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 256
print('Ответ:', N * v, 'байт')
