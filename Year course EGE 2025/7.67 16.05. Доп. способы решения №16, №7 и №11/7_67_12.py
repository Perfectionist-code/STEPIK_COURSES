from math import ceil, log2

size = 1280 * 960
k = 2048
i = ceil(log2(k))
v = size * i
tr_sp = 96_468_992
t = 132
for n in range(1, 10000):
    if v * n / tr_sp > t:
        print(n - 1)
        break
