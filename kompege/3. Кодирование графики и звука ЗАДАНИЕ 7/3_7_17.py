sp = 32_000
i = 16
k = 2
nu = 48_000
t = 90
v = k * i * nu * t
t_tr = v / sp
print('Ответ', t_tr // 60)
