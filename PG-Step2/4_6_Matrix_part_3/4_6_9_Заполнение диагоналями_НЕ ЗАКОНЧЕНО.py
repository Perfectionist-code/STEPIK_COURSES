n, m = map(int, input().split())  # Ввод размеров матрицы
matrix = [[0 for _ in range(m)] for _ in range(n)]  # Создание матрицы

num = 1  # Начальное значение для заполнения

# Заполнение матрицы по диагоналям
for d in range(n + m - 1):  # Количество диагоналей
    if d < m:  # Верхняя часть матрицы (включая главную диагональ)
        i = 0
        j = d
    else:  # Нижняя часть матрицы
        i = d - m + 1
        j = m - 1

    while i < n and j >= 0:
        matrix[i][j] = num
        num += 1
        i += 1
        j -= 1

# Вывод матрицы с форматированием
for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end='')
    print()