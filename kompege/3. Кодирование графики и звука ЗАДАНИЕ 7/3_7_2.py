from math import ceil, log2

size = 768 * 600
v = 420 * 2 ** 13
i = v // size
print('Ответ:', 2 ** i)
