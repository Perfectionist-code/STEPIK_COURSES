from math import log2, floor, ceil

size = 480 * 768
v = 405 * 2 ** 13
i = int(v / size)
i_2 = int(2 * i / 3)
num_colors = 2 ** i_2
print('Ответ: ', num_colors)
