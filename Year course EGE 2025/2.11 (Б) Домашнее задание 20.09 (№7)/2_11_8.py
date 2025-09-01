from math import ceil

v = 14 * 1024
v_pack = 2000
N = ceil(v / v_pack)
print('Ответ:', 2 * 60 * N)
