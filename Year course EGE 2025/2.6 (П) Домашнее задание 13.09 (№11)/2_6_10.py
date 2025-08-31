from math import ceil, log2

k = 2 * 26 + 10
i = ceil(log2(k))
n1 = 35
n2 = 27
N1 = 4
N2 = 5
V = 320
for v_add in range(1000):
    if ceil(i * n1 / 8) * N1 + ceil(i * n2 / 8) * N2 + v_add * (N1 + N2) > 320:
        print('Ответ:', v_add, 'байт')
        break
