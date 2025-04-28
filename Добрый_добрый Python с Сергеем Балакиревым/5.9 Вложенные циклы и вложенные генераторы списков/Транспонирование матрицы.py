# Транспонирование матрицы

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for row in A:
    print(*row, sep = '\t')
print()
A = [[row[i] for row in A] for i in range(len(A[0]))]

for row in A:
    print(*row, sep = '\t')