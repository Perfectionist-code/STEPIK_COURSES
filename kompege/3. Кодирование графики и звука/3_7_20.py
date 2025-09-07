k = 2
nu = 80_000
t = 3 * 60 + 25
V = 80 * 2 ** 23
for i in range(1, 300):
    if k * i * nu * t > V:
        print('Ответ', i - 1)
        break
