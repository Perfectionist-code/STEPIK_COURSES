from math import ceil, log2

size = 320 * 240
k = 256
i = ceil(log2(k))
v = ceil(size * i / 8)
V = 27 * 2 ** 20
for n in range(1, 3600):
    N = 3600 // n
    if v * N < V:
        print(n)
        break