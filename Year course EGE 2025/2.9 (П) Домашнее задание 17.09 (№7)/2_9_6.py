from math import ceil, log2

v = 3 * 2 ** 23
num_colors = 1_000_000
i = ceil(log2(num_colors))
V = int(v / 0.8)
size = 1080 * 920
v_col = size * i
v_transparency = V - v_col
i_transparency = v_transparency // size
print('Ответ:', 2 ** i_transparency)
