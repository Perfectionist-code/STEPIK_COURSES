from math import ceil, log2

k = 19 + 2
i = ceil(log2(k))
n = 17
v_1 = ceil(n * i / 8)
v_dp = 485
N = 4096
v = v_1 + v_dp
print('Ответ:', v * N // 2 ** 10)
