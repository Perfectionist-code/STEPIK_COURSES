n = int(input())
matr = [[0] * n for _ in range(n)]
for i in range(n):
    matr[i][n - i - 1] = 1
    matr[i][n - i:] = [2] * i

for row in matr:
    print(*row)


# n = int(input())
# matrix = [[None for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i + j + 1 == n:
#             matrix[i][j] = 1
#         elif i + j + 1 < n:
#             matrix[i][j] = 0
#         else:
#             matrix[i][j] = 2
#
# for row in matrix:
#     print(*row)