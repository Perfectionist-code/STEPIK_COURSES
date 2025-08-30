from math import ceil, log2

n = 22
k = 16
i = ceil(log2(k))
v = ceil(n * i / 8)
V = 700
print('Ответ:', V // v, 'пользователей')
