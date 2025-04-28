# Значимый подвиг 7. В программе инициализируется двумерное игровое поле размером N x N (N - натуральное число читается из входного потока), представленное в виде вложенного списка:
#
# P = [[0] * N for i in range(N)]
# Требуется расставить на поле P случайным образом M = 10 единиц (целочисленных) так, чтобы они не соприкасались друг с другом (то есть, вокруг каждой единицы должны быть нули, либо граница поля).
#
# P.S. Поле на экран выводить не нужно (вообще ничего не нужно выводить), только сформировать.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.3.7
#
# Sample Input:
#
# 10
# Sample Output:
#
# True

import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = int(input())
P = [[0] * N for i in range(N)]

count = 0

while count < 10:
    a, b = random.randrange(0, N, 2), random.randrange(0, N, 2)
    if P[a][b] == 1:
        continue
    P[a][b] = 1
    count += 1

# import random as rnd
#
# rnd.seed(1)
# N = int(input())
# P, M, deltas = [[0] * N for i in range(N)], 10, (-1, 0, 1)
#
# while M:
#     r, c = map(rnd.randrange, (N,) * 2)
#     if all(not (0 <= r + dr < N and 0 <= c + dc < N)
#            or P[r + dr][c + dc] == 0 for dr in deltas for dc in deltas):
#         P[r][c], M = 1, M - 1
[print(*i) for i in P]


