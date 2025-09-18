from math import ceil, log2

k = 26
i = ceil(log2(k))
n = 25
v = ceil(n * i / 8)
N = 35
print('Ответ:', v * N)