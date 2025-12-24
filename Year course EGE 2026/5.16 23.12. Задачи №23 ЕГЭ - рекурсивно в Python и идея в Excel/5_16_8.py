def f(curr: int, end: int):
    if curr < end: return 0
    if curr == end: return 1
    return f(curr - 2, end) + f(curr // 2, end)


print(f(38, 10) * f(10, 2))

f = [0] * 39
f[38] = 1
for i in range(38, 10, -1):
    if i - 2 >= 10: f[i - 2] += f[i]
    if i // 2 >= 10: f[i // 2] += f[i]
for i in range(10, 2, -1):
    if i - 2 >= 2: f[i - 2] += f[i]
    if i // 2 >= 2: f[i // 2] += f[i]

print(f[2])
