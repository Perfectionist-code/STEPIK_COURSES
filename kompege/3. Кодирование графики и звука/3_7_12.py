from math import ceil, log2

size = 480 * 768
V = 405 * 2 ** 13
i = V // size
i_col = 2 * (i // 3)
print('Ответ', 2 ** i_col)

