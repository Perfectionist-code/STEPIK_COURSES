n, m = int(input()), int(input())
matr = [[int(x) for x in input().split()] for j in range(n)]
i_c, j_c = map(int, input().split())
temp_matr = list(zip(*matr))
temp_matr[i_c], temp_matr[j_c] = temp_matr[j_c], temp_matr[i_c]
for row in zip(*temp_matr):
    print(*row)

# n, m = int(input()), int(input())
# matrix = [input().split() for _ in range(n)]
# col1, col2 = [int(i) for i in input().split()]
#
# for i in range(n):
#     matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
#
# for row in matrix:
#     print(*row)