n, m = map(int,input().split())
matr1 = [[int(x) for x in input().split()] for j in range(n)]
input()
matr2 = [[int(l) for l in input().split()] for k in range(n)]
matr_c = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        matr_c[i][j] = matr1[i][j] + matr2[i][j]
for row in matr_c:
    print(*row)
