from math import ceil, log2

size = 1536 * 2048
v = 6 * 2 ** 23
i = v // size
print('Ответ', 2 ** i)