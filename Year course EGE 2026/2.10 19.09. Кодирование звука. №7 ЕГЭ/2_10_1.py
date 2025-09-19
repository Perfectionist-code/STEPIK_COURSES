k = 2
nu = 48_000
i = 24
v = 288 * 2 ** 23
t = v / (k * i * nu * 60)
print('Ответ:', round(t))
