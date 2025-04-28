def rotating_matrix(*args):
    matr.reverse()
    return zip(*matr)


n = int(input())
matr = [[int(x) for x in input().split()] for j in range(n)]
for row in rotating_matrix(matr, n):
    print(*row)


# put your python code here
# n = int(input())
# x=[[*map(int,input().split())]for _ in '.'*n]
# for i in range(n):
#   print(*[x[j][i] for j in range(n)][::-1])

# n = int(input())
# matrix = [input().split() for _ in range(n)]
# result = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         result[i][j] = matrix[n - j - 1][i]
#
# for row in result:
#     print(*row)