from math import ceil, log2

n = 105
k = 10 + 1500
i = ceil(log2(k))
v = ceil(n * i / 8)
N = 16384
print('Ответ: ', int(v * N / 2 ** 10))
