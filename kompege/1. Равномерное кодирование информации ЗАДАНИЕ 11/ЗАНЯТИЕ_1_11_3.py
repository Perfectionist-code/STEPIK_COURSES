from math import log2, ceil

from mpmath.libmp.libhyper import complex_ei_taylor

id = 101
n = 10 + 4090
users = 2048
i = ceil(log2(n))
v_id = ceil(id * i / 8)
res = users * v_id
print('Ответ: ', res / 2 ** 10, 'Кбайт')
