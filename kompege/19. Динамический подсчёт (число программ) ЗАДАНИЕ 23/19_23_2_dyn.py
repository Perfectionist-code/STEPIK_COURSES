f = [0] * 155
f[5] = 1
for i in range(5, 154):
    if i + 1 <= 154: f[i + 1] += f[i]
    if i * 2 <= 154: f[i * 2] += f[i]
    if i ** 2 <= 154: f[i ** 2] += f[i]

print(f[154])
