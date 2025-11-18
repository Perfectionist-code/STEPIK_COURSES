from math import ceil, log2

size = 1280 * 1024
tr_sp = 1_966_080
n = 39
t = 280
for i in range(1, 1000):
    if size * i * n / tr_sp > t:
        print(2 ** (i - 1))
        break
