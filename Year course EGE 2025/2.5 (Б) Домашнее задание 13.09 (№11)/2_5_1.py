from math import ceil, log2

n = 10
k = 21 + 10
i = ceil(log2(k))
v = ceil(n * i / 8)
V = v * 81
print('Ответ:', V)
