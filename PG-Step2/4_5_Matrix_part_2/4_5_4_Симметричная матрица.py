def is_symmetrical(*args):
    for i in range(n):
        for j in range(n):
            if i != j and matr[i][j] != matr[j][i]:
                return False
    return True


n = int(input())
matr = [[int(x) for x in input().split()] for j in range(n)]
print(('NO', 'YES')[is_symmetrical(matr)])
