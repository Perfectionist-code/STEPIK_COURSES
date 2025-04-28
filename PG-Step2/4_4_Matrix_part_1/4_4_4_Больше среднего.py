from statistics import mean
n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
for row in matrix:
    cnt = 0
    # row_arithmetic_mean = sum(row) / n    # или используя эту строку
    for num in row:
        if float(num) > mean(row):          # тогда здесь функцию mean() заменить на row_arithmetic_mean
           cnt += 1
    print(cnt)