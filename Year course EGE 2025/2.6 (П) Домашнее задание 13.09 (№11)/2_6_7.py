from math import ceil, log2

n = 9
k = 26 * 2 + 10
i = ceil(log2(k))
v_pass = ceil(n * i / 8)
v_add = 18
v = v_pass + v_add
V = 2 << 9
for N in range(1000):
    if v * N > V:
        print('Ответ:', N - 1, 'пользователей')
        break
