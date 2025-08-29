from math import log2, ceil

from mpmath.libmp.libhyper import complex_ei_taylor

k = 10 + 2 * 26
i = ceil(log2(k))
N = 10
v = ceil(N * i / 8)
V = int(870/30)
v_dp = (V - v)
print('Ответ: ',v_dp ,'байт')



