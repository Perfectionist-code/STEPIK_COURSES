f = [0] * 21
f[2] = 1
for i in range(2,10):
    if i + 1 <= 10: f[i + 1] += f[i]
    if i + 3 <= 10: f[i + 3] += f[i]
for i in range(10,20):
    if i == 15: f[i] = 0
    if i + 1 <= 20: f[i + 1] += f[i]
    if i + 3 <= 20: f[i + 3] += f[i]

print('Ответ:', f[20])
