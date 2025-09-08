from math import ceil, log2

size = 1600 * 1200
num_colors = 1500
i = ceil(log2(num_colors))
v = ceil(size * i / 2 ** 13)
print('Ответ', v)
