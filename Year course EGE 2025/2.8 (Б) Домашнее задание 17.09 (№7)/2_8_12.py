from math import log2, floor, ceil

size = 1280 * 1024
v = 800 * 2 ** 13
i = int(v / size)
i_2 = i - 1
num_colors = 2 ** i_2
print('Ответ: ', num_colors)
