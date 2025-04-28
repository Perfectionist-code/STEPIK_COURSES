from string import ascii_lowercase

y, x = input()
y = ascii_lowercase.index(y)
x = int(x) - 1
matr = [['.' for _ in range(8)] for __ in range(8)]
matr[x][y] = 'N'
for i in range(8):
    for j in range(8):
        if abs((x - i) * (y - j)) == 2:
            matr[i][j] = '*'

# Блок вывода на печать
for row in matr[::-1]:
    print(*row)
