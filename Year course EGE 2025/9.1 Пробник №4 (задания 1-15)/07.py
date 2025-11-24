from math import ceil, log2

size = 768 * 5120
k = 256
i = ceil(log2(k))
tr_sp = 655_360
t = 500
for n in range(1, 1000):
    if i * size * n / tr_sp > t:
        print(n - 1)
        break
