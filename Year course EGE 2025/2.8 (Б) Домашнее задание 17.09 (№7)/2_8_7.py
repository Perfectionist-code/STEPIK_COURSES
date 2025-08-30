from math import log2, floor, ceil

size = 320 * 512
v_file = 50 * 2 ** 13
v = v_file * 1.55
i = int(v/size)
print(i)
num_colors = 2 ** i
print('Ответ: ', num_colors)
