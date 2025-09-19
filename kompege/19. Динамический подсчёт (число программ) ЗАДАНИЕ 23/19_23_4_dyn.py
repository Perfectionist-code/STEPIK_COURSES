f = [0] * 24
f[23] = 1
for i in range(23, 2, -1):
    if i - 2 >= 2: f[i - 2] += f[i]
    if i - 5 >= 2: f[i - 5] += f[i]

print(f[2])
