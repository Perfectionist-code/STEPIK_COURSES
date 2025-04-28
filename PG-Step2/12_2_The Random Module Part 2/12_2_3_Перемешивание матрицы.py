# from random import shuffle, sample
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# shuffle(matrix)
# matrix = [sample(row, len(row)) for row in matrix]

from random import shuffle

from sympy import flatten

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
temp = flatten(matrix)  # Переводим матрицу в одномерный список
# temp = sum(matrix, [])
shuffle(temp)
cnt = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = temp[cnt]
        cnt += 1

print(matrix)



# import random as rnd
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# n, m, lst = len(matrix), len(matrix[0]), sum(matrix, [])
# rnd.shuffle(lst)
# matrix = [[lst[i * m + j] for j in range(m)] for i in range(n)]