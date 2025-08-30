from math import ceil, log2

n = 34
k = 10 + 26
i = ceil(log2(k))
N = 10240
V = 20 * 2 << 19
for v_add in range(1,10000):
    if (ceil(n * i / 8) + v_add) * N == V:
        print('Ответ:', v_add)
        break