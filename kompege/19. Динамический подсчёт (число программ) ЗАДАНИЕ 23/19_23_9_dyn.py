f = [0] * 103
f[102] = 1
for i in range(102, 43, -1):
    if i - 8 >= 43: f[i - 8] += f[i]
    if i // 2 >= 43: f[i // 2] += f[i]
for i in range(43, 5, -1):
    if i - 8 >= 5: f[i - 8] += f[i]
    if i // 2 >= 5: f[i // 2] += f[i]

print(f[5])
