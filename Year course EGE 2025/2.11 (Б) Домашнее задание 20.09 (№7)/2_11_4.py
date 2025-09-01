k = 2
nu = 44_000
V = 82 * 2 ** 23
t = 5 * 60 + 25
for i in range(1, 192):
    if k * nu * t * i > V:
        print('Ответ:', i - 1, 'бит')
        break
