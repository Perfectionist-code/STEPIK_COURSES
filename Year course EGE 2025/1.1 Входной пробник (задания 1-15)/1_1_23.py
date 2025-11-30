f = [0] * 29
f[4] = 1
for i in range(4, 11):
    if i + 1 <= 11: f[i + 1] += f[i]
    if i + 4 <= 11: f[i + 4] += f[i]
    if i * 2 <= 11: f[i * 2] += f[i]
for i in range(11, 28):
    if i == 18: f[i] = 0
    if i + 1 <= 28: f[i + 1] += f[i]
    if i + 4 <= 28: f[i + 4] += f[i]
    if i * 2 <= 28: f[i * 2] += f[i]
print(f[28])
