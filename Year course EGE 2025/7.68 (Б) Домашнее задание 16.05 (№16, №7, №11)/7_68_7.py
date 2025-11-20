from math import ceil, log2

size = 1024 * 768
k = 4096
i = ceil(log2(k))
tr_sp = 1_310_720
t = 300
for n in range(1, 10000):
    if size * i * n / tr_sp > t:
        print(n - 1)
        break
