n = int(input())
matr = [[int(x) for x in input().split()] for _ in range(n)]
res = list(zip(*matr))

for row in res:
    print(*row)


# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n):
#     for j in range(i, n):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
# for row in matrix:
#     print(*row)