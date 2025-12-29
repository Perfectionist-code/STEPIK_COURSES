from math import ceil, log2

size = 1280 * 960
k = 2048
i = ceil(log2(k))
v = size * i
v_tr = 96_468_992
T = 132
for n in range(1, 1000):
    if v * n / v_tr > T:
        print(n - 1)
        break
