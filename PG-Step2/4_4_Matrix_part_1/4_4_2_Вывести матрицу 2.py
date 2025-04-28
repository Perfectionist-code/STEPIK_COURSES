n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for __ in range(n)]
for row in matrix:
    print(*row)
print()

for row in [*zip(*matrix)]:
    print(*row)

# но можно и  так
# for row in range(m):
#     for col in range(n):
#         print(matrix[col][row], end = ' ')
#     print()