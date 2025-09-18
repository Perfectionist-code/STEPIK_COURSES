from math import ceil, log2

k = 26
i = ceil(log2(k))
n = 16
v = ceil(i * n / 8)
V = 500
for N in range(300):
    if v * N > V:
        print('Ответ:', N - 1)
        break
