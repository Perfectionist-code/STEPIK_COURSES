n = int(input())
matr = [[int(x) for x in input().split()] for i in range(n)]
res1, res2, res3, res4 = [], [], [], []
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            res1.append(matr[i][j])
        elif j > i > n - 1 - j:
            res4.append(matr[i][j])
        elif j < i < n - 1 - j:
            res2.append(matr[i][j])
        if i > j and i > n - 1 - j:
            res3.append(matr[i][j])
print('Верхняя четверть:', sum(res1))
print('Правая четверть:', sum(res4))
print('Нижняя четверть:', sum(res3))
print('Левая четверть:', sum(res2))
