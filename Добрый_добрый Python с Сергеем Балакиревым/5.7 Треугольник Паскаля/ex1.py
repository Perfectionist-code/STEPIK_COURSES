n = int(input('Введите количество строк: '))
print('\n')

triangle = [[1] * (i+1) for i in range(n)]

for row in range(n):
    for cell in range(1, row):
        triangle[row][cell] = triangle[row-1][cell-1] + triangle[row-1][cell]

width = len(' '.join(map(str, triangle[-1])))

for row in triangle:
    print(' '.join(map(str,3 row)).center(width + 2))