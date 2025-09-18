from math import ceil, log2

k = 10 + 4090
i = ceil(log2(k))
n = 35
v_1 = ceil(n * i / 8)
N = 300
V = 96_000
V_1p = V // N
v_dp = V_1p - v_1
print('Ответ:', v_dp)
