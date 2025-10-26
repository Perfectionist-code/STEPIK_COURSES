from math import ceil, log2

n = 102
N = 282_952
V = 53 * 2 ** 20
for i in range(1000):
    if ceil(i * n // 8) * N > V:
        print(i - 1, 2 ** (i - 1))
        break

# ОТВЕТ: 32768