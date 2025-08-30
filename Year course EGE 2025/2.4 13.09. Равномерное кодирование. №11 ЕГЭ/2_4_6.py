from math import ceil, log2

n = 252
k = 10 + 1700
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 4096
print('Ответ: ', int(v * N / 2 ** 10), 'Кбайт')
