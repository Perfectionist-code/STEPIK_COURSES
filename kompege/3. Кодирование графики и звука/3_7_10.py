from math import ceil, log2

size  = 640 * 256
V = 170 * 2 ** 13
for i in range(1, 300):
    v = size * i / 1.35
    if v > V:
        print('Ответ', 2 ** (i - 1))
        break
