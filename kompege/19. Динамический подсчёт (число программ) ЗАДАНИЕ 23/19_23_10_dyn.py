f = [0] * 64
f[1] = 1
for i in range(1, 25):
    if i == 6: f[i] = 0
    if i + 2 <= 25: f[i + 2] += f[i]
    if i * 3 <= 25: f[i * 3] += f[i]
for i in range(25, 63):
    if i + 2 <= 63: f[i + 2] += f[i]
    if i * 3 <= 63: f[i * 3] += f[i]

print(f[63])
