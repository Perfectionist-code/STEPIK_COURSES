f = [0] * 16
f[1] = 1
for i in range(1, 15):
    if i + 1 <= 15: f[i + 1] += f[i]
    if i + 3 <= 15: f[i + 3] += f[i]
    if i * 2 <= 15: f[i * 2] += f[i]

print(f[15])