from math import log2, ceil

k = 10 + 26 + 450
i = ceil(log2(k))

N = 708
V = 213 * 2 << 9
for n in range(1000):
    if ceil(n * i / 8) * N > V:
        print('Ответ:', n)
        break
