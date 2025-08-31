from math import ceil, log2

t1 = 20
t2 = 24 * 3600
N = len(range(0, t2, t1))
size = 1920 * 1080
num_colors = 2048
i = ceil(log2(num_colors))
v_z = 5 * 2 << 9
v_image = ceil(size * i / 8)
v_file = v_image + v_z
V = ceil(v_file * N / (2 << 19))
print('Ответ:', V, 'Мбайт')
