from math import ceil, log2

n = 107
k = 10 + 2090
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 32_768
V = v * N // 2 ** 10
print('Ответ:', V, 'Кбайт')
