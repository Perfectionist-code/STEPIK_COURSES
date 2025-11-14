from math import ceil, log2

size = 1200 * 1600
k = 2000
i = ceil(log2(k))
v = size * i
v_comp = v * 0.79
v_zag = 20 * 2 ** 13
V = v_comp + v_zag
print(ceil(V/2**23))
