from math import log2, floor, ceil

size = 1024 * 768
num_colors = 2 ** 24
i = ceil(log2(num_colors))
num_transparency = 256
i_2 = ceil(log2(num_transparency))
v = ceil((i + i_2) * size / 2 ** 13)
print('Ответ: ', v, 'кб')
