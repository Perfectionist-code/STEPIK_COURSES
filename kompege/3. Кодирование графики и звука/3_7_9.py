from math import ceil, log2

size = 192 * 960
V = 90 * 2 ** 13
for i in range(1, 300):
    v = size * i * 0.65
    if v > V:
        print('Ответ', 2 ** (i - 1))
        break
