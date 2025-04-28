n, m = map(int, input().split())
matr = [['.' for x in range(m)] for j in range(n)]
start = 1
for i in range(n):
    for j in range(start, m, 2):
        matr[i][j] = '*'
    if start == 1:
        start = 0
    else:
        start = 1

# Блок вывода на печать
for row in matr:
    print(*row)


# n, m = [int(i) for i in input().split()]
# board = [['.'] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(1 - i % 2, m, 2):
#         board[i][j] = '*'
#
# for row in board:
#     print(*row)