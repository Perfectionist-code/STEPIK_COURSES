f = [0] * 46
f[13] = 1
for i in range(13, 45):
    if i == 16: f[i] = 0
    if i + 2 <= 45: f[i + 2] += f[i]
    if i * 3 <= 45: f[i * 3] += f[i]
    if i * 2 <= 45: f[i * 2] += f[i]

print('Ответ:', f[45])
