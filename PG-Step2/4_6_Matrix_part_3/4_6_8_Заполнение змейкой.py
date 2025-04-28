n, m = map(int, input().split())  # Ввод размеров матрицы
matrix = [[0 for _ in range(m)] for _ in range(n)]  # Создание матрицы

num = 1  # Начальное значение для заполнения

for i in range(n):
    if i % 2 == 0:  # Если строка четная, заполняем слева направо
        for j in range(m):
            matrix[i][j] = num
            num += 1
    else:  # Если строка нечетная, заполняем справа налево
        for j in range(m - 1, -1, -1):
            matrix[i][j] = num
            num += 1

# Вывод матрицы с форматированием
for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end='')
    print()