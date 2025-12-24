def f(curr: int, end: int):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr * 2, end) + f(curr * 3, end)


print(f(1, 18))

f = [0] * 19
f[1] = 1
for i in range(1, 18):
    if i + 1 <= 18: f[i + 1] += f[i]
    if i * 2 <= 18: f[i * 2] += f[i]
    if i * 3 <= 18: f[i * 3] += f[i]
print(f[18])
