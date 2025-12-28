from math import ceil, log2

n = 22
k = 16
i = ceil(log2(k))
v = ceil(i * n / 8)
V = 700
N = V//v
print(N)
