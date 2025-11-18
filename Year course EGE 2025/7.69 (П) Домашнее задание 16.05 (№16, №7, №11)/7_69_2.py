from math import ceil, log2

k = 2 * 26 + 10 + 1
i = ceil(log2(k))
V = 320
v_35 = ceil(35 * i / 8)
v_27 = ceil(27 * i / 8)
for v_zag in range(1, 1000):
    if 4 * (v_35 + v_zag) + 5 * (v_27 + v_zag) > V:
        print(v_zag)
        break
