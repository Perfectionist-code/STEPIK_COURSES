def f(curr: int, end: int):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr * 2, end)


print(f(1, 16))

f = [0] * 17
f[1] = 1

for i in range(1, 16):
    if i + 1 <= 16: f[i + 1] += f[i]
    if i * 2 <= 16: f[i * 2] += f[i]

print(f[16])
