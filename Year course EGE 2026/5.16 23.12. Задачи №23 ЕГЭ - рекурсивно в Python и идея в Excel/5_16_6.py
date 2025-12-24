def f(curr: int, end: int):
    if curr > end or curr == 21: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr * 3, end) + f(curr * 4, end)


print(f(2, 16) * f(16, 60))

f = [0] * 61
f[2] = 1
for i in range(2, 16):
    if i + 1 <= 16: f[i + 1] += f[i]
    if i * 3 <= 16: f[i * 3] += f[i]
    if i * 4 <= 16: f[i * 4] += f[i]
for i in range(16, 60):
    f[21] = 0
    if i + 1 <= 60: f[i + 1] += f[i]
    if i * 3 <= 60: f[i * 3] += f[i]
    if i * 4 <= 60: f[i * 4] += f[i]
print(f[60])
