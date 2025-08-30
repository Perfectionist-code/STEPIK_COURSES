from math import ceil, log2
n = 87
i = ceil(log2(n))
N = 64
v = N * i / 8
print('Ответ: ', ceil(v), 'байт')