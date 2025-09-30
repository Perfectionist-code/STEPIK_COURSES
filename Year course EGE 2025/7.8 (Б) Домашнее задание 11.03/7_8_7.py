from math import ceil, log2

k = 10 + 52 + 964
i = ceil(log2(k))
V = 1.5 * 2 ** 20
for n in range(1, 1000):
    if ceil(i * n / 8) * 3000 > V:
        print('Ответ:', n - 1)
        break
