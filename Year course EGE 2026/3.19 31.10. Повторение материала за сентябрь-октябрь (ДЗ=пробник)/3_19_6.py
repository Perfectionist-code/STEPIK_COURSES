from math import ceil, log2

size = 1024 * 768
k = 4096
t_rt = 1_310_720
i = ceil(log2(k))
v = size * i
T = 300
for n in range(500):
    if v * n / t_rt > T:
        print(n - 1)
        break
