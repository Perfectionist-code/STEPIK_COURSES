from math import ceil, log2

k = 10 + 70
i = ceil(log2(k))
N = 1_234_567
V = 24 * 2 ** 20
for n in range(1, 1000):
    if ceil(n * i / 8) * N > V:
        print(n)
        break
