from math import ceil, log2

size = 320 * 240
num_colors = 256
i = ceil(log2(num_colors))
v = ceil(size * i / 8)
V = 27 * 2 ** 20
for n in range(1, 3601):
    N = 3600 // n
    if v * N <= V:
        print('Ответ:', n, 'c')
        break
