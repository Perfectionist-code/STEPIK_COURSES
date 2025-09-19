f = [0] * 30
f[3] = 1
for i in range(3, 27):
    if i + 1 <= 27: f[i + 1] += f[i]
    if i + 4 <= 27: f[i + 4] += f[i]
    if i * 2 <= 27: f[i * 2] += f[i]
print('Ответ:', f[27])
