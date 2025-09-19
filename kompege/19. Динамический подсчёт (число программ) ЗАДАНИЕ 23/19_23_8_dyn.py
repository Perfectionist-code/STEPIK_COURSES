f = [0] * 21
f[3] = 1
for i in range(1, 9):
    if i + 1 <= 9: f[i + 1] += f[i]
    if i + 3 <= 9: f[i + 3] += f[i]
    if i * 2 <= 9: f[i * 2] += f[i]
for i in range(9, 12):
    if i + 1 <= 12: f[i + 1] += f[i]
    if i + 3 <= 12: f[i + 3] += f[i]
    if i * 2 <= 12: f[i * 2] += f[i]
for i in range(12, 20):
    if i + 1 <= 20: f[i + 1] += f[i]
    if i + 3 <= 20: f[i + 3] += f[i]
    if i * 2 <= 20: f[i * 2] += f[i]

print(f[20])
