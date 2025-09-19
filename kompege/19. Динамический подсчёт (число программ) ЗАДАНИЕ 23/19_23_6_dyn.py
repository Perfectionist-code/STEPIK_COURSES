f = [0] * 21
f[1] = 1
for i in range(1, 10):
    if i + 1 <= 10: f[i + 1] += f[i]
    if i * 2 <= 10: f[i * 2] += f[i]
for i in range(10, 200):
    if i + 1 <= 20: f[i + 1] += f[i]
    if i * 2 <= 20: f[i * 2] += f[i]
print(f[20])
