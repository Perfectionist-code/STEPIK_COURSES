from math import ceil, log2

k = 36
i = ceil(log2(k))
n = 12
v = ceil(i * n / 8)
V = 400
for N in range(300):
    if v * N > V:
        print('Ответ:', N - 1)
        break