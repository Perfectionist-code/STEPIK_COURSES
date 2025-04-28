from string import ascii_lowercase

y, x = input()
y = ascii_lowercase.index(y)
x = int(x) - 1
matr = [['.' for _ in range(8)] for __ in range(8)]
for i in range(8):
    for j in range(8):
        if (x == i and y != j) or (x != i and y == j) or (abs(x-i) == abs(y-j)):
            matr[i][j] = '*'
matr[x][y] = 'Q'

# Блок вывода на печать
for row in matr[::-1]:
    print(*row)

# x, y = input()
# n = 8
# board = [['.'] * n for _ in range(n)]
# x = ord(x) - 97
# y = n - int(y)
#
# for i in range(n):
#     for j in range(n):
#         if i == y or j == x:
#             board[i][j] = '*'
#         elif abs(i - y) == abs(j - x):
#             board[i][j] = '*'
#
# board[y][x] = 'Q'
#
# for row in board:
#     print(*row)