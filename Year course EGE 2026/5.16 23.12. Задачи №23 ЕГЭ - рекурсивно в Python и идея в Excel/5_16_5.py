def f(curr: int, end: int):
    if curr > end or curr == 8: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 2, end) + f(curr + 3, end)


print(f(3, 15))

f = [0] * 16
f[3] = 1
for i in range(3, 15):
    f[8] = 0
    if i + 1 <= 15: f[i + 1] += f[i]
    if i + 2 <= 15: f[i + 2] += f[i]
    if i + 3 <= 15: f[i + 3] += f[i]

print(f[15])
