from math import ceil, log2

k = 10 + 1700
i = ceil(log2(k))
n = 252
v = ceil(n * i / 8)
N = 4096
print('Ответ:', v * N // 2 ** 10)
