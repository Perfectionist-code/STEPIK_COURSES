from math import log2, floor, ceil

size = 1280 * 1024
num_colors = 2 ** 32
i = ceil(log2(num_colors))

v_file = size * i * .6 / 2**23

print('Ответ: ', ceil(v_file), 'Мб')
