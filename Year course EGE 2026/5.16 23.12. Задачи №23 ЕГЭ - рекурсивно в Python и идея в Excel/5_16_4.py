def f(curr: int, end: int):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 2, end) + f(curr + 3, end)


print(f(5, 7) * f(7, 11))

f = [0] * 12
f[5] = 1
for i in range(5, 7):
    if i + 1 <= 7: f[i + 1] += f[i]
    if i + 2 <= 7: f[i + 2] += f[i]
    if i + 3 <= 7: f[i + 3] += f[i]
for i in range(7, 11):
    if i + 1 <= 11: f[i + 1] += f[i]
    if i + 2 <= 11: f[i + 2] += f[i]
    if i + 3 <= 11: f[i + 3] += f[i]
print(f[11])
