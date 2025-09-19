f = [0] * 39
f[2] = 1
for i in range(2, 38):
    if i + 1 <= 38: f[i + 1] += f[i]
    if i * 2 <= 38: f[i * 2] += f[i]
    if i ** 2 <= 38: f[i ** 2] += f[i]

print(f[38])
