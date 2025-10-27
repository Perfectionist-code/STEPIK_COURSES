from math import ceil

k = 4
nu = 33_000
i = 37
N = 30
t = 41 * 60 + 33
sp = 363_956_352
t_tr = 307
V_w_zg = ceil(sp * t_tr // 2**13)
print(V_w_zg)

V = ceil(k * nu * i * t // 2**13)
print(V)
for v_zg in range(10000000):
    if V + v_zg * N >= V_w_zg:
        print((v_zg))
        break

# print(ceil(((V_w_zg-V)/30)/2**10))

# Ответ: 405106
