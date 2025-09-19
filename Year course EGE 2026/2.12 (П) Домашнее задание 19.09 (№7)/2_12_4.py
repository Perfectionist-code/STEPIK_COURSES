k = 2
nu = 48_000
i = 16
v = 32 * 2 ** 23
V = int(v / 0.8)
# V = V * 2 ** 23
t = V / (k * i * nu)
k2 = 1
i2 = 16
nu2 = 24_000
V2 = k2 * i2 * nu2 * t * 0.6 / 2 ** 23
print(V2)
