from math import log2, floor, ceil

size = 940 * 680
v = 2 ** 23
i_2 = 8
i = int(v / size - 8)
num_colors = 2 ** i
print('Ответ: ', num_colors)
