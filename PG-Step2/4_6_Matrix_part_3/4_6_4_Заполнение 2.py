n, m = map(int, input().split())
matr = [[0] * m for _ in range(n)]
for i in range(n):
    cnt = i + 1
    for j in range(m):
        matr[i][j] = cnt
        cnt += n

for i in range(n):
    for j in range(m):
        print(str(matr[i][j]).ljust(3), end = '')
    print()


# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for j in range(m):
#     for i in range(n):
#         matrix[i][j] = j * n + i + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()
#


# n, m = [int(i) for i in input().split()]
# matrix = [
#     list(range(i + 1, i + 1 + n * (m - 1) + 1, n))
#     for i in range(n)
# ]
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=" ")
#     print()

# [[*map(print, *zip(*[iter(range(1,n*m+1))]*n))]for n,m in [map(int,input().split())]]