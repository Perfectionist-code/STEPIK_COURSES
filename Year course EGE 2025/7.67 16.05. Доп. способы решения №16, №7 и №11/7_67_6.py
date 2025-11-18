from math import ceil

n = 377
N = 23155
V = 5536 * 2 ** 10
for i in range(1, 100):
    if ceil(n * i / 8) * N > V:
        print(2**(i-1) + 1)
        break
