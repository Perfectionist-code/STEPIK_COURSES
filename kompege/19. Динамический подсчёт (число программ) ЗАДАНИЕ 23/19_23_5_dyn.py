f = [0] * 23
f[22] = 1
for i in range(22, 2, -1):
    if i - 1 >= 2: f[i - 1] += f[i]
    if i - 3 >= 2: f[i - 3] += f[i]
    if i // 3 >= 2: f[i // 3] += f[i]

print(f[2])
