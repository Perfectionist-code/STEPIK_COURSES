from math import log2, ceil

k = 87
i = ceil(log2(k))
n = 64
v = ceil(i * n / 8)
print('Ответ:', v)
