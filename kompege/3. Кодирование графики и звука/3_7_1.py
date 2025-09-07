from math import ceil, log2

size = 64 * 128
num_colors = 128
i = ceil(log2(num_colors))
print('Ответ:', size * i // 2 ** 13)
