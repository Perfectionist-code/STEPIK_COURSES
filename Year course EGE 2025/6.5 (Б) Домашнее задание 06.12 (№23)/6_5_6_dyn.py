f = [0] * 26
f[3] = 1
for i in range(3, 10):
    if i + 2 <= 10: f[i + 2] += f[i]
    if i + 3 <= 10: f[i + 3] += f[i]
    if i * 2 <= 10: f[i * 2] += f[i]
for i in range(10, 25):
    if i == 17: f[i] = 0
    if i + 2 <= 25: f[i + 2] += f[i]
    if i + 3 <= 25: f[i + 3] += f[i]
    if i * 2 <= 25: f[i * 2] += f[i]

print('Ответ:', f[25])


print(f)