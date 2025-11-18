from math import ceil

size = 1920*1080
i = 16
v = ceil(size * i / 8)
V = 4 * 2 ** 30
N = 5_915_000
n_card = V // v
n = ceil(N / n_card)
print(n)