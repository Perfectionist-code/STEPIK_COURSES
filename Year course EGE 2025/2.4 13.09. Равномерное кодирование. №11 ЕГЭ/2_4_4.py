from math import ceil, log2

n = 7
k = 18 + 10
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 60
print('Ответ: ', v * N, 'байт')
