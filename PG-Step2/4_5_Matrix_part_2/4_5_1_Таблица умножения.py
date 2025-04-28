n, m = int(input()), int(input())
matr = [[i * j for i in range(m)] for j in range(n)]
for r in range(n):
    for c in range(m):
        print(str(matr[r][c]).ljust(3), end = ' ')
    print()