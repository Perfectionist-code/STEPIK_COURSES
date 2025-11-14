from math import log2, ceil

n = 99
k = 10 + 510
i = ceil(log2(k))
v = ceil(i * n / 8)
N = 4322
V = 543 * 2 ** 10
for d in range(1, 1000):
    if (v + d) * N > V:
        print(d)
        break
