from math import ceil, log2

size = 1920 * 1080
num_colors = 65_536
i = ceil(log2(num_colors))
V = 4 * 2 ** 30

v_image = ceil(i / 8) * size
v_images_catalog = v_image * 100
v_ost = V % v_images_catalog
print('Ответ:', v_ost // 2 ** 10, 'кбайт')
