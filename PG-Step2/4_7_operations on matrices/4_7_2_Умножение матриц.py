n, m = map(int,input().split())
matr1 = [[int(x) for x in input().split()] for j in range(n)]
input()
m1, k = map(int,input().split())
matr2 = [[int(l) for l in input().split()] for k1 in range(m1)]
matr_c = [[0] * k for i in range(n)]
# for row in matr_c:
#     print(*row)
# print()
# for row in matr1:
#     print(*row)
# print()
# for row in matr2:
#     print(*row)
# # print(matr1)
# # print(matr2)
for i in range(n):
    for j in range(k):
        # print(i, j, [matr1[i][k] * matr2[k][j] for k in range(min(m, m1))])
        matr_c[i][j] = sum([matr1[i][k] * matr2[k][j] for k in range(min(m, k))])
for row in matr_c:
    print(*row)


# n, m = [int(i) for i in input().split()]
# matrixA = [[int(i) for i in input().split()] for _ in range(n)]
# input()
# m, k = [int(i) for i in input().split()]
# matrixB = [[int(i) for i in input().split()] for _ in range(m)]
# matrixC = [[0] * k for _ in range(n)]
#
# for i in range(n):
#     for j in range(k):
#         for q in range(m):
#             matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
#
# for row in matrixC:
#     print(*row)