# def exchange_diagonals(*args):
#     matr1 = [[*x] for x in zip(*matr)]
#     for i in range(n):
#         matr1[i][i], matr1[i][n - i - 1] = matr1[i][n - i - 1], matr1[i][i]
#     return zip(*matr1)


def exchange_diagonals(*args):
    for i in range(n):
        matr[i][i], matr[n - i - 1][i] = matr[n - i - 1][i], matr[i][i]
    return matr

n = int(input())
matr = [[int(x) for x in input().split()] for j in range(n)]
for row in exchange_diagonals(matr):
    print(*row)
