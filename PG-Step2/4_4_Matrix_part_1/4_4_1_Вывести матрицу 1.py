n, m = int(input()), int(input())
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = input()
for row in matrix:
    print(*row)


# n = int(input())
# m = int(input())
#
# [print(*[input() for i in range(m)]) for i in range(n)]

# n, m = int(input()), int(input())
# matrix = [[input() for _ in range(m)] for _ in range(n)]
#
# for row in matrix:
#     print(*row)