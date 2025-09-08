from math import ceil, log2

size = 1024 * 120
V = 210 * 2 ** 13
i_tr = 7
i_total = V // size
i = i_total - i_tr
print('Ответ', 2 ** i)
