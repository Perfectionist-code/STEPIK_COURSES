def spiral_matrix(n, m):
    # Создаем матрицу размером n x m, заполненную нулями
    matrix = [[0 for _ in range(m)] for _ in range(n)]

    # Начальные значения
    num = 1
    top, bottom = 0, n - 1
    left, right = 0, m - 1

    while num <= n * m:
        # Движение вправо
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Движение вниз
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Движение влево
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Движение вверх
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix

n, m = map(int, input().split())
result = spiral_matrix(n, m)
for row in result:
    print(*row, sep = '\t')

# def generate_spiral_matrix(N):
#     matrix = [[0] * N for _ in range(N)]
#     row, col = 0, 0
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # вправо, вниз, влево, вверх
#     direction_idx = 0
#
#     for num in range(1, N*N + 1):
#         matrix[row][col] = num
#         next_row, next_col = row + directions[direction_idx][0], col + directions[direction_idx][1]
#
#         if 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col] == 0: # первые два условия для исключения выхода за границу матрицы, третье условие - проверка, чтобы не упёрлись в уже заполненную ячейку матрицы
#             row, col = next_row, next_col
#         else:
#             direction_idx = (direction_idx + 1) % 4  # изменить направление
#             row += directions[direction_idx][0]
#             col += directions[direction_idx][1]
#
#     return matrix
#
# for row in generate_spiral_matrix(int(input())):
#     print(*row, sep='\t')