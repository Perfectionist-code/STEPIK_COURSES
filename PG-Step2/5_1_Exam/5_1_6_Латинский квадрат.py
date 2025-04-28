def is_latin_square(*args):
    t_matr = list(zip(*matr))
    for i in range(n):
        for j in range(1, n + 1):
            if j not in matr[i] or j not in t_matr[i]:
                return False
    return True


n = int(input())
matr = [[int(x) for x in input().split()] for j in range(n)]
print(('NO', 'YES')[is_latin_square(matr, n)])




# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# numbers = list(range(1, n + 1))
# result = 'YES'
#
# for i in range(n):
#     row_nums = sorted(matrix[i])
#     col_nums = sorted([matrix[j][i] for j in range(n)])
#     if row_nums != numbers or col_nums != numbers:
#         result = 'NO'
#         break
#
# print(result)