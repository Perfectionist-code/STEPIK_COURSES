from math import ceil, log2

n = 25
k = 26
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 35
print('Ответ: ', v * N, 'байт')
