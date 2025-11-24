# from functools import lru_cache
#
# @lru_cache(None)
# def f(curr, end):
#     if curr < end or curr == 42: return 0
#     if curr == end: return 1
#     return f(curr - 1, end) + f(curr // 3, end) + f(curr // 4, end)
#
# for i in range(2025,25,-1): f(2025,i)
#
# print(f(2025,250) * f(250,25))

f = [0] * 2026
f[2025] = 1
for i in range(2025, 250, -1):
    if i == 42: f[i] = 0
    if i - 1 >= 250: f[i - 1] += f[i]
    if i // 3 >= 250: f[i // 3] += f[i]
    if i // 4 >= 250: f[i // 4] += f[i]
for i in range(250, 25, -1):
    if i == 42: f[i] = 0
    if i - 1 >= 25: f[i - 1] += f[i]
    if i // 3 >= 25: f[i // 3] += f[i]
    if i // 4 >= 25: f[i // 4] += f[i]

print(f[25])
print(f)
