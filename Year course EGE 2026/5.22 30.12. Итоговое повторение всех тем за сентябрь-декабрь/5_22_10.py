from math import ceil

n = 105
N = 65_536
V = 7 * 2 ** 20
for i in range(1, 1000):
    if ceil(i * n / 8) * N > V:
        print(2 ** (i - 1) + 1)
        break
