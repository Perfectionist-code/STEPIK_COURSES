from math import ceil, log2

k = 21 + 10
i = ceil(log2(k))
n = 10
v = ceil(n * i / 8)
N = 81
print('Ответ: ', v * N, 'байт')
