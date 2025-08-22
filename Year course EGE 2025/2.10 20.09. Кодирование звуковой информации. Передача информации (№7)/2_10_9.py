k = 4
i = 16
nu = 48_000
t = 3 * 60
sp = 3_200
v = k * i * nu * t
t_transmit = v / sp
print('Ответ:', t_transmit / 3600, 'час')
