f = [0] * 16
f[2] = 1
for i in range(2, 4):
    if i + 1 <= 4: f[i + 1] += f[i]
    if i + 2 <= 4: f[i + 2] += f[i]
    if i * 3 <= 4: f[i * 3] += f[i]
for i in range(4, 11):
    if i + 1 <= 11: f[i + 1] += f[i]
    if i + 2 <= 11: f[i + 2] += f[i]
    if i * 3 <= 11: f[i * 3] += f[i]
for i in range(11, 15):
    if i + 1 <= 15: f[i + 1] += f[i]
    if i + 2 <= 15: f[i + 2] += f[i]
    if i * 3 <= 15: f[i * 3] += f[i]

print('Ответ:', f[15])
