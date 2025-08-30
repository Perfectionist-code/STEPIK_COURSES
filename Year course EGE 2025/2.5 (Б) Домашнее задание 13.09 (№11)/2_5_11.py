from math import ceil

n = 197
N = 178_080
V = 25 * 2 << 19
for i in range(100):
    if ceil(n * i / 8) * N >= V:
        print('Ответ:', 2 ** (i - 1) + 1)
        break
