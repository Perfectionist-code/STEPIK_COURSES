from math import log2, ceil

n = 261
N = 252_500
V = 31 * 2 << 19
for i in range(1000):
    if ceil(n * i / 8) * N > V:
        print('Ответ:', 2 ** (i - 1) + 1)
        break
