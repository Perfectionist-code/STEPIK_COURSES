from math import log2, floor

size = 640 * 320
num_colors = 64
i = floor(log2(64))
v = size * i / 2 ** 13
print('Ответ: ', round(v), 'кбайт')
