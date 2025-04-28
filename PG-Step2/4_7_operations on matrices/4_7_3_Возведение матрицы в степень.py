def is_matrix_product(matr_1: list, matr_2: list):
    """
    Matrix product function
    :param matr_1: Matrix 1 is a list type
    :param matr_2: Matrix 2 is a list type
    :return: matrix (list) The result of the product of two matrices of size nxn
    """
    matr_c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matr_c[i][j] = sum([matr_1[i][k] * matr_2[k][j] for k in range(n)])
    return matr_c


n = int(input())
matr1 = [[int(x) for x in input().split()] for _ in range(n)]
_power = int(input())
res_matr = [[1 if i == j else 0 for j in range(n)] for i in
            range(n)]  # Создаём единичную матрицу для первой итерации или возведения в первую степень

for _ in range(_power):
    res_matr = is_matrix_product(res_matr,
                                 matr1)  # Вызываем функцию перемножения матриц согласно степени возведения матрицы

for row in res_matr:
    print(*row)


# def square_matrix_mult(matrixA, matrixB, size):
#     matrixC = [[0] * size for _ in range(size)]
#     for i in range(size):
#         for j in range(size):
#             for q in range(size):
#                 matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
#     return matrixC
#
#
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# m = int(input())
# powered_matrix = matrix.copy()
#
# for _ in range(m - 1):
#     powered_matrix = square_matrix_mult(matrix, powered_matrix, n)
#
# for row in powered_matrix:
#     print(*row)