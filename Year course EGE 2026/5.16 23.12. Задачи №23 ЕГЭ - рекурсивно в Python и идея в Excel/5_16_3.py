def f(curr: int, end: int):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 2, end) + f(curr * 3, end)


print(f(3, 9) * f(9, 14))

f = [0] * 15
f[3] = 1
for i in range(3, 9):
    if i + 1 <= 9: f[i + 1] += f[i]
    if i + 2 <= 9: f[i + 2] += f[i]
    if i * 3 <= 9: f[i * 3] += f[i]
for i in range(9, 14):
    if i + 1 <= 14: f[i + 1] += f[i]
    if i + 2 <= 14: f[i + 2] += f[i]
    if i * 3 <= 14: f[i * 3] += f[i]
print(f[14])
