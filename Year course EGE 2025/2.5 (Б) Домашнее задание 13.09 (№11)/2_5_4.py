from math import ceil, log2

n = 60
k = 10 + 250
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 65_536
V = v * N // 2 ** 10
print('Ответ:', V, 'Кбайт')
