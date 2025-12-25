def f(curr: int, end: int):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 3, end) + f(curr * 2, end)


print(f(2, 6) * f(6, 10)*f(10, 14))

f = [0] * 15
f[2] = 1
for i in range(2, 6):
    if i + 1 <= 6: f[i + 1] += f[i]
    if i + 3 <= 6: f[i + 3] += f[i]
    if i * 2 <= 6: f[i * 2] += f[i]
for i in range(6, 10):
    if i + 1 <= 10: f[i + 1] += f[i]
    if i + 3 <= 10: f[i + 3] += f[i]
    if i * 2 <= 10: f[i * 2] += f[i]
for i in range(10, 14):
    if i + 1 <= 14: f[i + 1] += f[i]
    if i + 3 <= 14: f[i + 3] += f[i]
    if i * 2 <= 14: f[i * 2] += f[i]

print(f[14])
