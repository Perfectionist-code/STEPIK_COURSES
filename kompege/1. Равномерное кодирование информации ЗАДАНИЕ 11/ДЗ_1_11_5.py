from math import log2, ceil

n1 = 11
k1 = 26 * 2 + 10
i1 = ceil(log2(k1))
v1 = ceil(n1 * i1 / 8)
v2 = min((ceil(len(bin(120)[2:]) / 8), ceil(log2(len(range(1, 121))) / 8)))
V = 28
v = v1 + v2
for v_add in range(100):
    if v + v_add == V:
        print('Отвте:', v_add)
