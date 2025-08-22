from math import log2, floor

size = 1024 * 768
num_colors = 4096
n = 256
i = floor(log2(num_colors))
v_paket = size * i * n / 2 ** 23
print('Ответ: ', round(v_paket), 'Мбайт')
