from math import ceil

t = 5 * 60
k = 4
nu = 40_000
i = 16
v = k * i * nu * t
print('Ответ', ceil(v / 2 ** 23))
