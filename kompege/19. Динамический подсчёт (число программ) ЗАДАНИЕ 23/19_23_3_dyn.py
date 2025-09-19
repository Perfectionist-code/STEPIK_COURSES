f = [0] * 14
f[1] = 1
for i in range(1, 13):
    if i + 1 <= 13: f[i + 1] += f[i]
    if i + 2 <= 13: f[i + 2] += f[i]
    if i * 4 <= 13: f[i * 4] += f[i]

print(f[13])
