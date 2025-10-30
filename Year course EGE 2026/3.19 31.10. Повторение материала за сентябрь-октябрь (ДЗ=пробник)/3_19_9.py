from math import ceil, log2

n = 2783
N = 3_845_627
V = 11 * 2 ** 30
for i in range(1, 500):
    v = ceil(i * n / 8)
    if v * N >= V:
        print(2 ** (i - 1) + 1)
        break
