n, m = int(input()), int(input())
matr = [[int(x) for x in input().split()] for j in range(n)]
max_num = -1e26
for i, row in enumerate(matr):
    for j, num in enumerate(row):
        if num > max_num:
            max_num = num
            i_max = i
            j_max = j
print(i_max, j_max)

