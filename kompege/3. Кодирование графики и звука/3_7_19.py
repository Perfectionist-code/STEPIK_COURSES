k = 2
nu = 44_000
t = 5 * 60 + 25
V = 82 * 2 ** 23
for i in range(1, 300):
    if k * nu * i * t > V:
        print('Ответ', i - 1)
        break
