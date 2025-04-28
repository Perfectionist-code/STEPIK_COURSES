n = int(input())
matr = [[int(x) for x in input().split()] for i in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if (j <= i <= n - 1 - j) or (j >= i >= n - 1 - j):
            res.append(matr[i][j])
print(max(res))





