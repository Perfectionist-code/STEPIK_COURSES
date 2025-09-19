f = [0] * 31
f[1] = 1
for i in range(1, 12):
    if i + 1 <= 12: f[i + 1] += f[i]
    if i * 2 <= 12: f[i * 2] += f[i]
for i in range(12, 30):
    if i + 1 <= 30: f[i + 1] += f[i]
    if i * 2 <= 30: f[i * 2] += f[i]

print(f[30])
