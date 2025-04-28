from sympy import flatten
n = int(input())
print(max(flatten([[int(x) for x in input().split()[:i + 1]] for i in range(n)])))

# Моё второе решение
# n = int(input())
# matrix = [[int(x) for x in input().split()] for i in range(n)]
# max_num = -1e26
# for i, row in enumerate(matrix):
#     max_num_row = max(row[:i + 1])
#     if max_num_row > max_num:
#         max_num = max_num_row
# print(max_num)




