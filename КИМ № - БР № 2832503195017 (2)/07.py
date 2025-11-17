from math import ceil, log2

i1 = 16
t = 60
k2 = 256

V_1m = 12 * 2 ** 23
v_f = V_1m // 60
size = ceil(v_f / i1)
i2 = ceil(log2(k2))
print(i2)

