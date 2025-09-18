from math import ceil, log2

k = 8
i = ceil(log2(k))
n = 15
v = ceil(i * n / 8)
v_dp = 24
v += v_dp
V = v * 20
print('Ответ:', V)

