n = int(input())
matr = [['.'] * n  for j in range(n)]
middle = n >> 1
for i in range(n):
    matr[i][i], matr[i][-1 -i], matr[i][middle] = '*', '*', '*'
    if i == middle:
        matr[i] = ['*'] * n
for row in matr:
    print(*row)

# n = int(input())
# matrix = [["." for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     # для главной диагонали
#     matrix[i][i] = "*"
#     # для побочной диагонали
#     matrix[i][n - 1 - i] = "*"
#     # для средней строки
#     matrix[n // 2][i] = "*"
#     # для среднего столбца
#     matrix[i][n // 2] = "*"
#
# for row in matrix:
#     print(*row)

# n = int(input())
# matrix = [['.'] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == n // 2 or j == n // 2:
#             matrix[i][j] = '*'
#         elif i == j or i + j + 1 == n:
#             matrix[i][j] = '*'
#
# for row in matrix:
#     print(*row)