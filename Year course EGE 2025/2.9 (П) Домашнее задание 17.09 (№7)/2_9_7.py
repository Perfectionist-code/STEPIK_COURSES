from math import ceil, log2

size = 2048 * 1536
v_add = 128 * 2 ** 13
N = 32
V = 16 * 2 ** 23

v_col = V // N - v_add
i = v_col * 4 // size
print('Ответ:', 2 ** i)
