from math import ceil, log2

size = 1024 * 960
tr_sp = 1_474_560
t = 140
n = 32
for i in range(1, 10000):
    if size * i * n / tr_sp > t:
        print(2 ** (i - 1))
        break
