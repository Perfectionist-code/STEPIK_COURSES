def is_symmetrical(*args):
    for i in range(n-1):
        for j in range(n-1):
            if matr[i][j] != matr[n - j - 1][n - i - 1]:
                return False
    return True


n = int(input())
matr = [[int(x) for x in input().split()] for j in range(n)]
print(('NO', 'YES')[is_symmetrical(matr)])


# def is_symmetric(matrix):
#     for i in range(n):
#         for j in range(n - i - 1):
#             if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
#                 return "NO"
#
#     return "YES"
#
#
# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# print(is_symmetric(matrix))

# nn = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(nn)]
#
# lst = [matrix[i][i] for i in range(nn)]
# print('YES' if lst == lst[::-1] else 'NO')