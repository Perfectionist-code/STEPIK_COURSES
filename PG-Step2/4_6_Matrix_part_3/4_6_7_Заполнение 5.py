n, m = map(int, input().split())
matr = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matr[i][j] = (i + j) % m + 1
for j in range(n):
    for k in range(m):
        print(str(matr[j][k]).ljust(3), end = '')
    print()

# n, m = map(int, input().split())  # Ввод размеров матрицы
# matrix = [[0 for _ in range(m)] for _ in range(n)]  # Создание матрицы
#
# for i in range(n):
#     for j in range(m):
#         # Заполняем элемент матрицы
#         matrix[i][j] = (i + j) % m + 1
#
# # Вывод матрицы с форматированием
# for row in matrix:
#     for elem in row:
#         print(str(elem).ljust(3), end='')
#     print()


# n, m = [int(i) for i in input().split()]
# numbers = list(range(1, m + 1))
# matrix = []
#
# for _ in range(n):
#     matrix.append(numbers)
#     # переносим первый элемент списка в конец
#     numbers = numbers[1:] + [numbers[0]]
#
# for row in matrix:
#     print(*row)