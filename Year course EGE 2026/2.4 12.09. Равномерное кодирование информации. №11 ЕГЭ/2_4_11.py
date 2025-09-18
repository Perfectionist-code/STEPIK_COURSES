from math import ceil, log2

k = 10 + 2 * 26 + 6
i = ceil(log2(k))
n = 9
v_1 = ceil(n * i / 8)
N = 20
V_1p = 500 // N
v_dp = V_1p - v_1
print('Ответ:', v_dp)
