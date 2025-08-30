from math import log2, ceil

from mpmath.libmp.libhyper import complex_ei_taylor

n_chars = 2 * 26
n_pass = 7
i = ceil(log2(n_chars))
v = ceil(n_pass * i / 8)
v_user = v + 12
res = 2 * 2 ** 10 // v_user
print('Ответ:', res)
