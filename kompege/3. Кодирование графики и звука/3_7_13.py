from math import ceil, log2

size = 1536 * 1024
V = 9 * 2 ** 23
N = 60 // 10
v = V // N
i = v // size
print('Ответ', 2 ** i)
