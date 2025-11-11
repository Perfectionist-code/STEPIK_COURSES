from functools import lru_cache

@lru_cache(None)
def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr - 2, end) + f(curr * 2, end) + f(curr ** 2, end)

# for i in range(2, 25): f(2, i)

print(f(2, 25))

# f = [0] * 50000
# f[2] = 1
# for i in range(2, 25):
#     if i - 2 <= 25: f[i - 2] += f[i]
#     if i * 2 <= 25: f[i * 2] += f[i]
#     if i ** 2 <= 25: f[i ** 2] += f[i]
#
# print(f[25])
