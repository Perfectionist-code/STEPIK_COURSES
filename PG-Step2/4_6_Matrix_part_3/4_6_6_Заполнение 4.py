n = int(input())
matr = [[0] * n for _ in range(n)]
for i in range(n // 2 + 1):  # диапазон перебора делим пополам, для уменьшения количества итераций
    matr[i][i:n - i] = [1] * (n - 2 * i)  # заполняем строки согласно условию в прямом направлении (сверху вниз)
    matr[-i - 1][i:n - i] = [1] * (n - 2 * i)  # одновременно заполняем зеркально снизу вверх до середины
for j in range(n):
    for k in range(n):
        print(str(matr[j][k]).ljust(3), end = '')
    print()

# n = int(input())
# matrix = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if (i <= j and i + j + 1 <= n) or (i >= j and i + j + 1 >= n):
#             matrix[i][j] = 1
#
# for i in range(n):
#     for j in range(n):
#         print(str(matrix[i][j]).ljust(3), end = ' ')
#     print()