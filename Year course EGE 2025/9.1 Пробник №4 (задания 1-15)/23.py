def f(curr, end):
    if curr < end: return 0
    if curr == end: return 1
    return f(curr - 2, end) + f(curr // 2, end)

print(f(50,11)*f(11, 2))

# f = [0] * 51
# f[50] = 1
#
# for i in range(50, 11, -1):
#     if i - 2 >= 11: f[i - 2] += f[i]
#     if i // 2 >= 11: f[i // 2] += f[i]
# for i in range(11, 2, -1):
#     if i - 2 >= 2: f[i - 2] += f[i]
#     if i // 2 >= 2: f[i // 2] += f[i]
#
# print(f[2])
# print(f)
