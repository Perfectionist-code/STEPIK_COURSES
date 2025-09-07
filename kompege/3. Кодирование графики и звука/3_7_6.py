from math import ceil, log2

num_colors = 1600
i = ceil(log2(num_colors))
size = 480 * 640
v = ceil(size * i / 2 ** 13)
print('Ответ', v)
