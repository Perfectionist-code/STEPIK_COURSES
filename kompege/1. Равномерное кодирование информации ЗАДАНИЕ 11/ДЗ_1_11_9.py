from math import log2, ceil

n = 101
k = 10 + 4090
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 2048
V = v * N
print('Ответ:', V // (2 << 9), 'Кбайт')
