n = int(input()) + 1
triangle = [[1] * (i+1) for i in range(n)]

for row in range(n):
    for cell in range(1, row):
        triangle[row][cell] = triangle[row-1][cell-1] + triangle[row-1][cell]

print(triangle[n-1])


# # -------------------ФУНКЦИЯ-------------------
# def pascal(n):
#     triangle = [[1]]
#
#     for i in range(n):
#         row = [1]
#         for j in range(1, len(triangle[i])):
#             row += [sum(triangle[i][j - 1: j + 1])]
#         row += [1]
#         triangle.append(row.copy())
#
#     return triangle[n]
#
#
# # --------------------ВЫЗОВ--------------------
# print(pascal(int(input())))