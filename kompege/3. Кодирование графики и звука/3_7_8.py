from math import ceil, log2

size = 3900 * 2160
v = 13 * 2 ** 23
i = v // size
print('Ответ', 2 ** i)