def is_mirroring(*args):
    for i in range(n >> 1):
        for j in range(n):
            matr[i][j], matr[n - i - 1][j] = matr[n - i - 1][j], matr[i][j]
    return matr


n = int(input())
matr = [[int(x) for x in input().split()] for j in range(n)]
for row in is_mirroring(matr, n):
    print(*row)
