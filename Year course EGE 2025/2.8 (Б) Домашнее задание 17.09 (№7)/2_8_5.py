from math import log2, floor, ceil

size = 640 * 480
num_colors = 65_536
i = ceil(log2(num_colors))
v = 10 * 2 ** 23
v_file = size * i + 60 * 2 ** 13
n = int(v / v_file)
print('Ответ: ', n, 'файлов')
