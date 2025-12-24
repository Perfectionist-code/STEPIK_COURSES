def f(curr: int, end: int):
    if curr < end or curr == 7: return 0
    if curr == end: return 1
    return f(curr - 1, end) + f(curr - 3, end) + f(curr // 2, end)


print(f(19, 10) * f(10, 3))

f = [0] * 20
f[19] = 1
for i in range(19, 10, -1):
    if i - 1 >= 10: f[i - 1] += f[i]
    if i - 3 >= 10: f[i - 3] += f[i]
    if i // 2 >= 10: f[i // 2] += f[i]

for i in range(10, 3, -1):
    f[7] = 0
    if i - 1 >= 3: f[i - 1] += f[i]
    if i - 3 >= 3: f[i - 3] += f[i]
    if i // 2 >= 3: f[i // 2] += f[i]

print(f[3])
