n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
# n - море
# m - деревня
# k - горы
# x - деревня море
# y - деревня горы
# z - ДВИ

# n, m, k, x, y, z = 14, 16, 5, 10, 3, 2
res = n - x + m - y + k + z
print(res)