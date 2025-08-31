from math import ceil, log2

t1 = 6
t2 = 24 * 3600
num_colors = 256
i = ceil(log2(num_colors))
n = t2 // t1
size = 128 * 256
v = size * i
V = v * n
print('Ответ:', V // 2 ** 23, 'Мбайт')
