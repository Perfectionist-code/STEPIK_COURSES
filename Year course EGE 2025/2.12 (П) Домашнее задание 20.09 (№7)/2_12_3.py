from math import ceil, log2

t = 4 * 60 + 16
k = 2
nu = 11_000
i = ceil(log2(65536))
v1 = ceil(k * nu * i * t / 8)
i2 = ceil(log2(1024))
nu2 = 44_000
v2 = ceil(k * nu2 * i2 * t / 8)
print('Ответ:', (v2 - v1) // 2 ** 10)
