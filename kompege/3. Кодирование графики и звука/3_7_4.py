from math import ceil, log2

i = 16
size = 640 * 480
n = 128
v = ceil(size * i / 8)
V = n * v
print('Ответ', ceil(V / 2 ** 20))
