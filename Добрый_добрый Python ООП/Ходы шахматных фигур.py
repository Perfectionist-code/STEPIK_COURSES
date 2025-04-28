chessboard = [list(input()) for _ in range(8)]

pieces = {'T': lambda i, j, x, y: '+' if x == j or y == i else '-',                    # для ладьи
          'S': lambda i, j, x, y: '+' if abs(x - j) == abs(y - i) else '-',            # для слона
          'F': lambda i, j, x, y: '+' if (abs(x - j) == abs(y - i) or                  # для ферзя
                                          (x == j or y == i)) else '-',
          'H': lambda i, j, x, y: '+' if (abs(x - j) == 1 and abs(y - i) == 2 or        # для коня
                                          abs(x - j) == 2 and abs(y - i) == 1) else '-'
         }

for i, row in enumerate(chessboard):
    for j, char in enumerate(row):
        if char != '-':
            x, y, piece = j, i, char
            break

for i in range(8):
    for j in range(8):
        chessboard[i][j] = pieces[piece](i, j, x, y)
chessboard[y][x] = piece

for row in chessboard:
    print(''.join(row))