n = int(input())
matr = [[0] * n for _ in range(n)]
for i in range(n):
    matr[i][n - i - 1] = 1
    matr[i][i] = 1

for i in range(n):
    for j in range(n):
        print(str(matr[i][j]).ljust(3), end = '')
    print()


# n = int(input())
# matrix = [[0 for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j + 1 == n:
#             matrix[i][j] = 1
#
# for row in matrix:
#     print(*row)


