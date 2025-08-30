from math import ceil, log2

n = 14
k = 26 * 2
i = ceil(log2(k))
v = ceil(n * i / 8)
V = 600
print('Ответ:', V // v, 'паролей')
