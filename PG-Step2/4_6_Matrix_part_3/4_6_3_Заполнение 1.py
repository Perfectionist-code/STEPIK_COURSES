n, m = map(int, input().split())
matr = [[0] * m for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(m):
        matr[i][j] = cnt
        cnt += 1

for i in range(n):
    for j in range(m):
        print(str(matr[i][j]).ljust(3), end = ' ')
    print()


# n, m = [int(i) for i in input().split()]
# matrix = [list(range(m*i + 1, m*i + 1 + m)) for i in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()

# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * m + j + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()